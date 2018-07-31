test = {
  'name': 'Car',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from car import *
          >>> hilfingers_car = Car('Tesla', 'Model S')
          >>> hilfingers_car.color
          80d498e7f8cbec95df437d78b524521a
          # locked
          >>> hilfingers_car.paint('black')
          1b93d7f83f69e1b06c11954d997cf04f
          # locked
          >>> hilfingers_car.color
          9ccdc90cb9022261857bac913f59ab65
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> from car import *
          >>> hilfingers_car = Car('Tesla', 'Model S')
          >>> hilfingers_car.model
          066daa99c4c14fba33ca7fea6de5139e
          # locked
          >>> hilfingers_car.gas = 10
          >>> hilfingers_car.drive()
          6782dfbb8a7616b3f504afa7bdbc4efe
          # locked
          >>> hilfingers_car.drive()
          8e18dc54497447151e91747068c581ce
          # locked
          >>> hilfingers_car.fill_gas()
          86623ae32a344b2c86ec58b8962d85fd
          # locked
          >>> hilfingers_car.gas
          2b5c8adf725274c931c4272b26ac97ea
          # locked
          >>> Car.gas
          e0c9124d3360b0721b517ec33d41b017
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> from car import *
          >>> hilfingers_car = Car('Tesla', 'Model S')
          >>> Car.headlights
          9338923f09aac77121029c604f7ce4f3
          # locked
          >>> hilfingers_car.headlights
          9338923f09aac77121029c604f7ce4f3
          # locked
          >>> Car.headlights = 3
          >>> hilfingers_car.headlights
          a6a221ff20ce085ab4bedaca5044f971
          # locked
          >>> hilfingers_car.headlights = 2
          >>> Car.headlights
          a6a221ff20ce085ab4bedaca5044f971
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> from car import *
          >>> hilfingers_car = Car('Tesla', 'Model S')
          >>> hilfingers_car.wheels = 2
          >>> hilfingers_car.wheels
          9338923f09aac77121029c604f7ce4f3
          # locked
          >>> Car.num_wheels
          612ff2a71cad53bc4c7f85fac678a06d
          # locked
          >>> hilfingers_car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          8e18dc54497447151e91747068c581ce
          # locked
          >>> Car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          8a2fd4e4c3c6dcce2dc631af62ee217a
          # locked
          >>> Car.drive(hilfingers_car) # Type Error if an error occurs and Nothing if nothing is displayed
          8e18dc54497447151e91747068c581ce
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
