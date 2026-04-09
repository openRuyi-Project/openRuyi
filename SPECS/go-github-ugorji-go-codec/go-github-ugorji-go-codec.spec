# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-codec
%define go_path         github.com/ugorji/go
%define go_import_path  github.com/ugorji/go/codec

Name:           go-github-ugorji-go-codec
Version:        1.2.14
Release:        %autorelease
Summary:        idiomatic codec and rpc lib for msgpack, cbor, json, etc.
License:        MIT
URL:            https://github.com/ugorji/go-codec
#!RemoteAsset
Source0:        https://github.com/ugorji/go-codec/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/ugorji/go/codec) = %{version}

Requires:       go(github.com/google/go-cmp)
Requires:       go(golang.org/x/tools)

%description
This repository contains the go-codec library, the codecgen tool and
benchmarks for comparing against other libraries.

This is a High Performance, Feature-Rich Idiomatic Go 1.20+
codec/encoding library for binary and text formats: binc, msgpack, cbor,
json and simple.

It supports generics and monomorphization, based on build tags set.

%package     -n go-codecgen
Summary:        Executable of codecgen

%description -n go-codecgen
This package contains the github.com/ugorji/go-codec module executables.

%prep -a
%__mkdir -p %{_builddir}/go/src/%{go_path}
%__cp -a . %{_builddir}/go/src/%{go_path}/

# Build binaries for codecgen tool
%build
%{go_common}
cd %{_builddir}/go/src/%{go_path}
go install -trimpath -v -p %{?_smp_build_ncpus} %{go_path}
go install -trimpath -v -p %{?_smp_build_ncpus} %{go_path}/codec
go install -trimpath -v -p %{?_smp_build_ncpus} %{go_path}/codec/codecgen

# Install binaries for codecgen tool
%install
# Same as above
install -d %{buildroot}%{go_sys_gopath}/%{go_path}
cp -a . %{buildroot}%{go_sys_gopath}/%{go_path}/
install -d %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/go/bin/codecgen %{buildroot}%{_bindir}/

%check
%{go_common}
cd %{_builddir}/go/src/%{go_path}
go test -vet=off -v %{go_path}/codec %{go_path}/codec/codecgen

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_path}

%files -n go-codecgen
%license LICENSE*
%{_bindir}/codecgen

%changelog
%autochangelog
