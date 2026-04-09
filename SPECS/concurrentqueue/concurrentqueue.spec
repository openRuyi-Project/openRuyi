# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           concurrentqueue
Version:        1.0.4
Release:        %autorelease
Summary:        A fast multi-producer, multi-consumer lock-free concurrent queue for C++11
License:        BSD-2-Clause
URL:            https://github.com/cameron314/concurrentqueue
#!RemoteAsset:  sha256:87fbc9884d60d0d4bf3462c18f4c0ee0a9311d0519341cac7cbd361c885e5281
Source0:        https://github.com/cameron314/concurrentqueue/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
A fast multi-producer, multi-consumer lock-free concurrent queue for C++11.
It's a header-only library.

%package        devel
Summary:        Development files for %{name}

%description    devel
Development files for concurrentqueue.


%files devel
%{_includedir}/concurrentqueue/
%{_libdir}/cmake/concurrentqueue/

%changelog
%autochangelog
