/*
 * Task.cpp
 *
 *  Created on: May 19, 2024
 *      Author: aoaaceai
 */

#include "Task.h"

namespace hitcon {
namespace service {
namespace sched {

Task::Task(unsigned prio, task_callback_t callback, void *thisptr)
		: prio(prio), callback(callback), thisptr(thisptr) {
	static unsigned lastTid = 0;
	tid = lastTid++;
}

Task::~Task() {

}

unsigned Task::GetTid() {
	return tid;
}

bool Task::operator ==(unsigned &tid) {
	return this->tid == tid;
}

bool Task::operator ==(Task &task) {
	return task == tid;
}

bool Task::operator <(Task &task) {
	return prio < task.prio;
}

void Task::Run() {
	callback(thisptr, arg);
}

void Task::SetArg(void *arg) {
	this->arg = arg;
}

} /* namespace sched */
} /* namespace service */
} /* namespace hitcon */
