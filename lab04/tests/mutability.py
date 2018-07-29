test = {
  'name': 'Mutability',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> lst = [5, 6, 7, 8]
          >>> lst.append(6)
          5c5b429063049b010ee9d6da4aff0f09
          # locked
          >>> lst
          8479bcf7fd6e046c0ee92e37bd0bd1c5
          # locked
          >>> lst.insert(0, 9)
          >>> lst
          34540cad83a3fb7bcbb40cf99a050929
          # locked
          >>> x = lst.pop(2)
          >>> lst
          8523dc04d1767396bf99d8d5f2753450
          # locked
          >>> lst.remove(x)
          >>> lst
          92986ceb5cb04366cd52ed70547eb7cc
          # locked
          >>> a, b = lst, lst[:]
          >>> a is lst
          46d1f016b6482a76a74835354edaab71
          # locked
          >>> b == lst
          46d1f016b6482a76a74835354edaab71
          # locked
          >>> b is lst
          61e74011ca20035e5cb51b814087a093
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> pokemon = {'pikachu': 25, 'dragonair': 148, 'mew': 151}
          >>> pokemon['pikachu']
          6958307009d94c1d298ae9f450f606ff
          # locked
          >>> len(pokemon)
          62cb7be5b3f27b8761401e9f99897a30
          # locked
          >>> pokemon['jolteon'] = 135
          >>> pokemon['mew'] = 25
          >>> len(pokemon)
          e6efc1fcfbebed28c5068a807b6cce64
          # locked
          >>> 'mewtwo' in pokemon
          61e74011ca20035e5cb51b814087a093
          # locked
          >>> 'pikachu' in pokemon
          46d1f016b6482a76a74835354edaab71
          # locked
          >>> 25 in pokemon
          61e74011ca20035e5cb51b814087a093
          # locked
          >>> 148 in pokemon.values()
          46d1f016b6482a76a74835354edaab71
          # locked
          >>> 151 in pokemon.keys()
          61e74011ca20035e5cb51b814087a093
          # locked
          >>> 'mew' in pokemon.keys()
          46d1f016b6482a76a74835354edaab71
          # locked
          >>> pokemon['ditto'] = pokemon['jolteon']
          >>> pokemon['ditto']
          311478efa7505dcdcb0779d4d503b284
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
