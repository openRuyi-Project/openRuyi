# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           fwd
%define go_import_path  github.com/philhofer/fwd

Name:           go-github-philhofer-fwd
Version:        1.2.0
Release:        %autorelease
Summary:        Buffered Reader/Writer
License:        MIT
URL:            https://github.com/philhofer/fwd
#!RemoteAsset
Source0:        https://github.com/philhofer/fwd/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/philhofer/fwd) = %{version}

%description

Package fwd provides a buffered reader and writer. Each has methods that
help improve the encoding/decoding performance of some binary protocols.

The Writer and Reader type provide similar functionality to their
counterparts in bufio, plus a few extra utility methods that simplify
read-ahead and write-ahead. I wrote this package to improve
serialization
performance for github.com/tinylib/msgp
(https://github.com/tinylib/msgp), where it provided about a 2x speedup
over bufio for certain workloads. However, care must be taken to
understand the semantics of the extra methods provided by this package,
as they allow the user to access and manipulate the buffer memory
directly.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
