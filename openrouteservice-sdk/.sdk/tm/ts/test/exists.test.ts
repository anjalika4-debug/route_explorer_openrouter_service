
import { test, describe } from 'node:test'
import { equal } from 'node:assert'


import { OpenrouteserviceSDK } from '..'


describe('exists', async () => {

  test('test-mode', () => {
    const testsdk = OpenrouteserviceSDK.test()
    equal(testsdk instanceof OpenrouteserviceSDK, true,
      'OpenrouteserviceSDK.test() must return a client synchronously')
  })

})
