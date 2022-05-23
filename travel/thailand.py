class ThailandPackage:
    def detail(self):
        print("태국 패키지 3박 4일, 방콕 파타야 여행 및 야시장 투어")

if __name__ == "__main__":
    print("Thailand 모듈을 직접 실행한다.")
    print("이 문장은 모듈을 직접 실행 시 실행됩니다.")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("Thailand 외부에서 모듈호출이 이루어졌습니다.")
    # 파일 외부에서 호출 시 여기가 호출된다.