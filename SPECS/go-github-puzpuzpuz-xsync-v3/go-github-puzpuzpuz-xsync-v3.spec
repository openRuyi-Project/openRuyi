# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           xsync
%define go_import_path  github.com/puzpuzpuz/xsync/v3

Name:           go-github-puzpuzpuz-xsync-v3
Version:        3.5.1
Release:        %autorelease
Summary:        Concurrent data structures for Go
License:        Apache-2.0
URL:            https://github.com/puzpuzpuz/xsync
#!RemoteAsset:  sha256:9b01fb25f5d0ea71c20810a4bcc62d116d6c39686f04e51f3b6620eefb39754d
Source0:        https://github.com/puzpuzpuz/xsync/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/puzpuzpuz/xsync/v3) = %{version}

%description
xsync/v3 provides concurrent maps, counters, and queues. MinIO uses the
v3 import path; the unversioned xsync package is already in the distro.

%prep -a
# Go 1.27 linker panics on TestMakeHashFunc (R_USEIFACE hashfunc.SS).
rm -f util_hash_test.go

%files
%doc README.md BENCHMARKS.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
