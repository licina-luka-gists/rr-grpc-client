from concurrent import futures

import grpc
import pingpong_pb2
import pingpong_pb2_grpc
import time
import threading

class Listener(pingpong_pb2_grpc.PingPongServiceServicer):
  def __init__(self, *args, **kwargs):
    self.counter = 0

  def ping(self, request, context):
    self.counter += 1
    return pingpong_pb2.Pong(count=request.count + 1)

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
  pingpong_pb2_grpc.add_PingPongServiceServicer_to_server(Listener(), server)

  server.add_insecure_port('[::]:9999')
  server.start()

  try:
    while True:
      print('Server running, act %i' % (threading.active_count()))
      time.sleep(10)
  except KeyboardInterrupt:
    print('Exited')
    server.stop(0)

if __name__ == '__main__':
  serve()
