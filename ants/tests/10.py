test = {
  'name': 'Problem 10',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'answer': '57340058c74192e31e9088794d23e3c0',
          'choices': [
            'A TankAnt does damage to all Bees in its place each turn',
            'A TankAnt has greater armor than a BodyguardAnt',
            'A TankAnt can contain multiple ants',
            'A TankAnt increases the damage of the ant it contains'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          Besides costing more to deploy, what is the only difference between a
          TankAnt and a BodyguardAnt?
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing TankAnt parameters
          >>> TankAnt.food_cost
          1417936d6fc6e9b3ac66b50e5d407ada
          # locked
          >>> TankAnt.damage
          10d7626438082950badf2b6216f9b0a8
          # locked
          >>> TankAnt.is_container
          154afc22815a37701b5fa71e532da526
          # locked
          >>> tank = TankAnt()
          >>> tank.armor
          1218df75a941ebc08cec539b1f16208f
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing TankAnt action
          >>> tank = TankAnt()
          >>> place = colony.places['tunnel_0_1']
          >>> other_place = colony.places['tunnel_0_2']
          >>> place.add_insect(tank)
          >>> for _ in range(3):
          ...     place.add_insect(Bee(3))
          >>> other_place.add_insect(Bee(3))
          >>> tank.action(colony)
          >>> [bee.armor for bee in place.bees]
          [2, 2, 2]
          >>> [bee.armor for bee in other_place.bees]
          [3]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing TankAnt container methods
          >>> tank = TankAnt()
          >>> thrower = ThrowerAnt()
          >>> place = colony.places['tunnel_0_1']
          >>> place.add_insect(thrower)
          >>> place.add_insect(tank)
          >>> place.ant is tank
          True
          >>> bee = Bee(3)
          >>> place.add_insect(bee)
          >>> tank.action(colony)   # Both ants attack bee
          >>> bee.armor
          1
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ants import *
      >>> beehive, layout = Hive(make_test_assault_plan()), dry_layout
      >>> dimensions = (1, 9)
      >>> colony = AntColony(None, beehive, ant_types(), layout, dimensions)
      >>> #
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing TankAnt action
          >>> tank = TankAnt()
          >>> place = colony.places['tunnel_0_1']
          >>> place.add_insect(tank)
          >>> for _ in range(3):
          ...     place.add_insect(Bee(1))
          >>> tank.action(colony)
          >>> len(place.bees)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing TankAnt.damage
          >>> tank = TankAnt()
          >>> tank.damage = 100
          >>> place = colony.places['tunnel_0_1']
          >>> place.add_insect(tank)
          >>> for _ in range(3):
          ...     place.add_insect(Bee(100))
          >>> tank.action(colony)
          >>> len(place.bees)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Placement of ants
          >>> tank = TankAnt()
          >>> harvester = HarvesterAnt()
          >>> place = colony.places['tunnel_0_0']
          >>> # Add tank before harvester
          >>> place.add_insect(tank)
          >>> place.add_insect(harvester)
          >>> colony.food = 0
          >>> tank.action(colony)
          >>> colony.food
          1
          >>> try:
          ...   place.add_insect(TankAnt())
          ... except AssertionError:
          ...   print("error!")
          error!
          >>> place.ant is tank
          True
          >>> tank.contained_ant is harvester
          True
          >>> try:
          ...   place.add_insect(HarvesterAnt())
          ... except AssertionError:
          ...   print("error!")
          error!
          >>> place.ant is tank
          True
          >>> tank.contained_ant is harvester
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Placement of ants
          >>> tank = TankAnt()
          >>> harvester = HarvesterAnt()
          >>> place = colony.places['tunnel_0_0']
          >>> # Add harvester before tank
          >>> place.add_insect(harvester)
          >>> place.add_insect(tank)
          >>> colony.food = 0
          >>> tank.action(colony)
          >>> colony.food
          1
          >>> try:
          ...   place.add_insect(TankAnt())
          ... except AssertionError:
          ...   print("error!")
          error!
          >>> place.ant is tank
          True
          >>> tank.contained_ant is harvester
          True
          >>> try:
          ...   place.add_insect(HarvesterAnt())
          ... except AssertionError:
          ...   print("error!")
          error!
          >>> place.ant is tank
          True
          >>> tank.contained_ant is harvester
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Removing ants
          >>> tank = TankAnt()
          >>> test_ant = Ant()
          >>> place = Place('Test')
          >>> place.add_insect(tank)
          >>> place.add_insect(test_ant)
          >>> place.remove_insect(test_ant)
          >>> tank.contained_ant is None
          True
          >>> test_ant.place is None
          True
          >>> place.remove_insect(tank)
          >>> place.ant is None
          True
          >>> tank.place is None
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> tank = TankAnt()
          >>> place = Place('Test')
          >>> place.add_insect(tank)
          >>> tank.action(colony) # Action without contained ant should not error
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # test proper call to death callback
          >>> original_death_callback = Insect.death_callback
          >>> Insect.death_callback = lambda x: print("insect died")
          >>> place = colony.places["tunnel_0_0"]
          >>> bee = Bee(3)
          >>> tank = TankAnt()
          >>> ant = ThrowerAnt()
          >>> place.add_insect(bee)
          >>> place.add_insect(ant)
          >>> place.add_insect(tank)
          >>> bee.action(colony)
          >>> bee.action(colony)
          insect died
          >>> bee.action(colony) # if you fail this test you probably didn't correctly call Ant.reduce_armor or Insect.reduce_armor
          insect died
          >>> Insect.death_callback = original_death_callback
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ants import *
      >>> beehive, layout = Hive(make_test_assault_plan()), dry_layout
      >>> dimensions = (1, 9)
      >>> colony = AntColony(None, beehive, ant_types(), layout, dimensions)
      >>> #
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
