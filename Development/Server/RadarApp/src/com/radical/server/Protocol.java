package com.radical.server;

public class Protocol {
	public static final byte CONNECT_PI = 0x01;
	public static final byte DISCONNECT_PI = 0x02;
	public static final byte CONNECT_CLIENT = 0x03;
	public static final byte DISCONNECT_CLIENT = 0x04;
	public static final byte SUBSCRIBE = 0x05;
	public static final byte UNSUBSCRIBE = 0x06;
	public static final byte DATA = 0x07;
	public static final byte GET_LAST = 0x08;
}