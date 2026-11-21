# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Run the upstream password-strength estimator suite via make test.
%define _test_target test

Name:           zxcvbn-c
Version:        2.6
Release:        %autorelease
Summary:        Password strength estimation library
License:        MIT
URL:            https://github.com/tsyrogit/zxcvbn-c
#!RemoteAsset:  sha256:11e39f6776f9c82c68b2acb94336e32697d4ab6cdb4ac16f9583ccbdd735113a
Source0:        https://github.com/tsyrogit/zxcvbn-c/archive/refs/tags/v%{version}.tar.gz#/zxcvbn-c-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(install):  PREFIX=%{_prefix}
BuildOption(install):  LIBDIR=%{_libdir}

BuildRequires:  gcc-c++
BuildRequires:  make

%description
zxcvbn-c estimates the difficulty of guessing passwords by recognizing
dictionary words, keyboard patterns, repetitions and common substitutions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers and a linker file for applications using the zxcvbn library.

# The release Makefile builds and installs the shared library directly.
%conf

%build -p
%{set_build_flags}

%install -a
rm -f %{buildroot}%{_libdir}/libzxcvbn.a

%files
%doc README.md
%license LICENSE.txt
%{_bindir}/zxcvbn-dictgen
%{_datadir}/zxcvbn/
%{_libdir}/libzxcvbn.so.*

%files devel
%{_includedir}/zxcvbn.h
%{_libdir}/libzxcvbn.so

%changelog
%autochangelog
