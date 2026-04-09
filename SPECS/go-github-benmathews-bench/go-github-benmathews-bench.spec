# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           bench
%define go_import_path  github.com/benmathews/bench
%define commit_id f7c75b9ef6e795bbf5de3556fa0c2d418a3e3331
# TODO: test dependency need too much dependency, add it later - Julian
%define go_test_ignore_failure 1

Name:           go-github-benmathews-bench
Version:        0+git20210120.f7c75b9
Release:        %autorelease
Summary:        A generic latency benchmarking library.
License:        Apache-2.0
URL:            https://github.com/benmathews/bench
#!RemoteAsset
Source0:        https://github.com/benmathews/bench/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/benmathews/bench) = %{version}

%description
Bench is a generic latency benchmarking library. It's generic in the
sense that it exposes a simple interface (Requester) which can be
implemented for various systems under test. Several example Requesters
(https://github.com/benmathews/bench/tree/master/requester) are provided
out of the box.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
