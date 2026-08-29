# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libffi
Version:        3.5.2
Release:        %autorelease
Summary:        A Portable Foreign Function Interface Library
License:        MIT
URL:            https://sourceware.org/libffi
VCS:            git:https://github.com/libffi/libffi
#!RemoteAsset
Source0:        https://github.com/libffi/libffi/releases/download/v%{version}/%{name}-%{version}.tar.gz
Buildsystem:    autotools

BuildOption(conf):  --disable-multi-os-directory
BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-exec-static-tramp

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  dejagnu
BuildRequires:  make

%description
Compilers for high level languages generate code that follows certain conventions. These
conventions are necessary, in part, for separate compilation to work. One such convention
is the "calling convention". The "calling convention" is a set of assumptions made by the
compiler about where function arguments will be found on entry to a function. A "calling
convention" also specifies where the return value for a function is found.

Some programs may not know at the time of compilation what arguments are to be passed to a
function. For instance, an interpreter may be told at run-time about the number and types
of arguments used to call a given function. Libffi can be used in such programs to provide
a bridge from the interpreter program to compiled code.

The libffi library provides a portable, high level programming interface to various calling
conventions. This allows a programmer to call any function specified by a call interface
description at run-time.

FFI stands for Foreign Function Interface. A foreign function interface is the popular name
for the interface that allows code written in one language to call code written in another
language. The libffi library really only provides the lowest, machine dependent layer of a
fully featured foreign function interface. A layer must exist above libffi that handles type
conversions for values passed between the two languages.

%package        devel
Summary:        Development files for libffi
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The devel package with header files and libraries is for developing apps which needs libffi.

%install -a
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%files
%license LICENSE
%{_libdir}/*.so.*

%files devel
%{_libdir}/pkgconfig/libffi.pc
%{_includedir}/ffi*.h
%{_libdir}/*.so
%{_mandir}/man3/*
%{_infodir}/libffi.info*

%changelog
%{?autochangelog}
