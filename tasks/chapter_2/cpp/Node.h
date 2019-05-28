//
// Created by Eugene on 2019-05-28.
//

#ifndef INTERVIEW_CHEAT_SHEET_NODE_H
#define INTERVIEW_CHEAT_SHEET_NODE_H

#include <initializer_list>
#include <sstream>
#include <string>
#include <vector>
#include <unordered_map>

template <class T>
class Node {
public:
    Node(T value);
    Node(std::initializer_list<T> l);
    ~Node();
    T getValue() const;
    void setValue(T value);
    void addToTail(T value);
    void setNext(Node<T>* next);
    std::string print() const;
    std::vector<T> toVector() const;
    Node<T>* removeDuplicates();
    Node<T>* removeDuplicatesWithoutBuffer();
    void selfDelete();
    Node<T>* find(T value);
    Node<T>* sort_around(T x);
    Node<T>* find_loop();
    bool is_palindrom();
protected:
    T value;
    Node* next;
};

template <class T> Node<T>::Node(T value):value(value) {
    this->next = nullptr;
};

template <class T> Node<T>::Node(std::initializer_list <T> l) {
    this->next = nullptr;

    bool currentInitialized = false;

    for(auto &element : l) {
        if (!currentInitialized) {
            this->value = element;
            currentInitialized = true;
        }
        else
            this->addToTail(element);
    }
};

template <class T> Node<T>::~Node() {
    auto cursor = this;
    if(cursor->next != nullptr) {
        delete cursor->next;
    }
}

template <class T> void Node<T>::addToTail(T value) {
    Node* cursor = this;
    while(cursor->next != nullptr) {
        cursor = cursor->next;
    }

    cursor->next = new Node<T>(value);
};

template <class T> T Node<T>::getValue() const {
    return this->value;
};

template <class T> std::string Node<T>::print() const {
    std::stringstream ss;
    auto cursror = this;
    ss << "[";
    while (cursror != nullptr) {
        ss << cursror->value << " -> ";
        cursror = cursror->next;
    }
    ss << "]";

    return ss.str();
};

template <class T> void Node<T>::setValue(T value) {
    this->value = value;
};

template <class T> std::ostream& operator<<(std::ostream& s, const Node<T>& t)
{
    s << t.print();
    return s;
}

template <class T> std::ostream& operator<<(std::ostream& s, const Node<T>* t)
{
    s << t->print();
    return s;
}

template <class T> std::vector<T> Node<T>::toVector() const {
    std::vector<T> result;


    for(auto cursor = this; cursor != nullptr; cursor = cursor->next)
        result.push_back(cursor->value);

    return result;
}

template <class T> Node<T>* Node<T>::removeDuplicates() {
	std::unordered_map<T, bool> buffer;

	Node<T>* prev = nullptr;
	for(auto cursor = this; cursor != nullptr; prev = cursor, cursor = cursor->next) {
		if(buffer[cursor->value]) {
			prev->next = cursor->next;
			cursor->next = nullptr;
			delete cursor;
			cursor = prev;
		} else
			buffer[cursor->value] = true;
	}

	return this;
}

template <class T> Node<T>* Node<T>::removeDuplicatesWithoutBuffer() {
	for(auto cursor = this; cursor != nullptr; cursor = cursor->next) {
        Node<T>* prev = cursor;
        for(auto internal_cursor = cursor->next; internal_cursor != nullptr; prev = internal_cursor, internal_cursor = internal_cursor->next)
			if(internal_cursor->value == cursor->value) {
				prev->next = internal_cursor->next;
				internal_cursor->next = nullptr;
				delete internal_cursor;
				internal_cursor = prev;
			}
	}

	return this;
}

template <class T> void Node<T>::selfDelete() {
    auto next_item = this->next;
    this->value = this->next->value;
    this->next = this->next->next;

    next_item->next = nullptr;
    delete next_item;
}

template <class T> Node<T>* Node<T>::find(T value) {
    if (this->value == value)
        return this;

    if (!this->next)
        return nullptr;

    return this->next->find(value);
}

template <class T> Node<T>* Node<T>::sort_around(T x) {
   Node<T>* less_x = nullptr;
   Node<T>* greater_x = nullptr;
   auto less_x_end = less_x;
    auto greater_x_end = greater_x;

   for(auto cursor = this; cursor != nullptr; cursor = cursor->next) {
       if (cursor->value < x) {
            if (less_x) {
                less_x_end->next = new Node<T>(cursor->value);
                less_x_end = less_x_end->next;
            } else {
                less_x = new Node<T>(cursor->value);
                less_x_end = less_x;
            }
       } else {
           if (greater_x) {
               greater_x_end->next = new Node<T>(cursor->value);
               greater_x_end = greater_x_end->next;
           } else {
               greater_x = new Node<T>(cursor->value);
               greater_x_end = greater_x;
           }
       }
   }

   if (!less_x)
       return greater_x;

   less_x_end->next = greater_x;

   return less_x;
}

template <class T> Node<T>* Node<T>::find_loop() {
    auto fast = this;
    auto slow = this;

    do {
        if(!fast->next || !fast->next->next)
            return nullptr;

        fast = fast->next->next;
        slow = slow->next;
    } while (fast != slow);

    slow = this;

    while (fast != slow) {
        fast = fast->next;
        slow = slow->next;
    }

    return fast;
}

template <class T> bool Node<T>::is_palindrom() {
    auto middle = this;
    auto end = this;

    if (!this->next) {
        return true;
    }

    while(end && end->next) {
        end = end->next->next;
        middle = middle->next;
    }

    bool result = true;

    Node<T>* first_part_start = nullptr;
    auto cursor = this;


    while(cursor != middle || (cursor == middle && end)) {
        if (!first_part_start) {
            first_part_start = new Node<T>(cursor->value);
        } else {
            auto new_item = new Node<T>(cursor->value);
            new_item->next = first_part_start;
            first_part_start = new_item;
        }

        if (cursor == middle)
            break;

        cursor = cursor->next;
    }

    auto first = first_part_start;
    while (middle) {
        if (middle->value != first->value) {
            result = false;
            break;
        }

        middle = middle->next;
        first = first->next;
    }

    delete first_part_start;

    return result;
}

template <class T> void Node<T>::setNext(Node<T>* next) {
    this->next = next;
}


#endif //INTERVIEW_CHEAT_SHEET_NODE_H
