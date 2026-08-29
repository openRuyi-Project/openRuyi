# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit0 9a42ec1329f259a5f4881a291db1dcb8f2ad9040
%global shortcommit0 9a42ec1
%global date0 20260623

Name:           cpp-threadpool
Version:        0+git%{date0}.%{shortcommit0}
Release:        %autorelease
Summary:        Simple C++11 thread pool implementation
License:        Zlib
URL:            https://github.com/progschj/ThreadPool
#!RemoteAsset:  sha256:954e0ecdac1aa0da1e0fa78577ff0d352e53094df43762fbc1884f76a7e1dcd2
Source0:        https://github.com/progschj/ThreadPool/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
BuildArch:      noarch
# Header-only library; explicit sections below override configure/build/install.
BuildSystem:    autotools

BuildRequires:  gcc-c++

%description
cpp-threadpool is a simple C++11 thread pool implementation distributed as a
single header.

%package        devel
Summary:        Development files for %{name}

%description    devel
This package contains the ThreadPool.h header.

%prep
%autosetup -n ThreadPool-%{commit0}

%conf
# Header-only library; no configure step.

%build
# Header-only library.

%install
install -d -m 0755 %{buildroot}%{_includedir}
install -p -m 0644 ThreadPool.h %{buildroot}%{_includedir}/ThreadPool.h

%check
%{__cxx} %{build_cxxflags} -std=c++11 -pthread example.cpp -I. -o threadpool-example
./threadpool-example >/dev/null

%files
%doc README.md
%license COPYING

%files devel
%{_includedir}/ThreadPool.h

%changelog
%autochangelog
