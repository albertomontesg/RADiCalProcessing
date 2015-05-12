//: Playground - noun: a place where people can play

import UIKit

var str = "hello";

class Connection : NSObject, NSStreamDelegate {
	let serverAddress: CFString = "127.0.0.1"
	let serverPort: UInt32 = 30000
	
	private var inputStream: NSInputStream!
	private var outputStream: NSOutputStream!
	
	func connect() {
		println("connecting...")
		
		var readStream:  Unmanaged<CFReadStream>?
		var writeStream: Unmanaged<CFWriteStream>?
		
		CFStreamCreatePairWithSocketToHost(nil, self.serverAddress, self.serverPort, &readStream, &writeStream)
		
		// Documentation suggests readStream and writeStream can be assumed to
		// be non-nil. If you believe otherwise, you can test if either is nil
		// and implement whatever error-handling you wish.
		
		self.inputStream = readStream!.takeRetainedValue()
		self.outputStream = writeStream!.takeRetainedValue()
		
		self.inputStream.delegate = self
		self.outputStream.delegate = self
		
		self.inputStream.scheduleInRunLoop(NSRunLoop.currentRunLoop(), forMode: NSDefaultRunLoopMode)
		self.outputStream.scheduleInRunLoop(NSRunLoop.currentRunLoop(), forMode: NSDefaultRunLoopMode)
		
		self.inputStream.open()
		self.outputStream.open()
	}
	
	func stream(stream: NSStream, handleEvent eventCode: NSStreamEvent) {
		println("stream event")
	}
}

var c = Connection()
c.connect()
c.outputStream
