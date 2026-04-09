# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libgee
Version:        0.20.8
Release:        %autorelease
Summary:        GObject collection library
License:        LGPL-2.1-or-later
URL:            https://wiki.gnome.org/Projects/Libgee
VCS:            git:https://gitlab.gnome.org/GNOME/libgee.git
#!RemoteAsset
Source:         https://download.gnome.org/sources/libgee/0.20/libgee-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --enable-vala
BuildOption(install):  typelibdir=%{_libdir}/girepository-1.0
BuildOption(install):  girdir=%{_datadir}/gir-1.0

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  vala

%description
libgee is a collection library providing GObject-based interfaces and
classes for commonly used data structures.

* Traversable
  o Iterable
    + Collection
      - List
        * BidirList
      - Set
        * SortedSet
          o BidirSortedSet
      - MultiSet
      - Queue
        * Deque
    + Map
      - SortedMap
        * BidirSortedMap
  o Iterator
    + BidirIterator
      - BidirListIterator
    + ListIterator
      - BidirListIterator
* MultiMap

The ArrayList, ArrauQueue, ConcurrentLinkedList, ConcurrentSet, HashSet,
HashMap, HashMultiSet, HashMultiMap, LinkedList, PriorityQueue, TreeSet,
TreeMap, TreeMultiSet, and TreeMultiMap classes provide a reasonable sample
implementation of those interfaces. In addition, a set of abstract
classes are provided to ease the implementation of new collections.

Around that, the API provide means to retrieve read-only views,
efficient sort algorithms, simple, bi-directional or index-based mutable
iterators depending on the collection type.

Libgee is written in Vala and can be used like any GObject-based C
library. It's planned to provide bindings for further languages.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep -a
find -name '*.vala' -exec touch {} \;

%conf -p
autoreconf -fiv

%files
%doc AUTHORS MAINTAINERS NEWS README
%license COPYING
%{_libdir}/*.so.*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Gee-0.8.typelib

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/gee-0.8.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Gee-0.8.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gee-0.8.vapi

%changelog
%autochangelog
