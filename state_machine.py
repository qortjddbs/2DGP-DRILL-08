from event_to_string import event_to_string

class StateMachine:
    def __init__(self, start_state, rules):
        self.cur_state = start_state
        self.cur_state.enter(('START', 0))  # 초기화할 땐 더미 이벤트 전달
        self.rules = rules

    def update(self):
        self.cur_state.do()

    def draw(self):
        self.cur_state.draw()

    def handle_state_event(self, state_event):
        for check_event in self.rules[self.cur_state].keys():
            if check_event(state_event):    # 만약 들어온 게 space_down 이면
                self.next_state = self.rules[self.cur_state][check_event]   # 스테이트 바꾸기
                self.cur_state.exit(state_event)   # 엑시트 액션 (필요시 이벤트 전달)
                self.next_state.enter(state_event) # 엔트리 액션 (필요시 이벤트 전달)
                print(f'{self.cur_state.__class__.__name__} - {event_to_string(state_event)} -> {self.next_state.__class__.__name__}')
                # 현재 상태 - 이벤트 -> 다음 상태 출력
                self.cur_state = self.next_state    # 상태 전환
                return # 상태 바꿨으면 나가기

        print(f'처리되지 않은 이벤트 {event_to_string(state_event)} 가 발생.')
        # 디버깅 용 출력
