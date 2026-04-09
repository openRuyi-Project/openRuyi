# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-iptables
%define go_import_path  github.com/coreos/go-iptables
# Test need root premission, ignore it - Julian
%define go_test_ignore_failure 1

Name:           go-github-coreos-go-iptables
Version:        0.8.0
Release:        %autorelease
Summary:        Go wrapper around iptables utility
License:        Apache-2.0
URL:            https://github.com/coreos/go-iptables
#!RemoteAsset
Source0:        https://github.com/coreos/go-iptables/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/coreos/go-iptables) = %{version}

%description
Go bindings for iptables utility.

In-kernel netfilter does not have a good userspace API. The tables are
manipulated via setsockopt that sets/replaces the entire table. Changes
to existing table need to be resolved by userspace code which is
difficult and error-prone. Netfilter developers heavily advocate using
iptables utlity for programmatic manipulation.

go-iptables wraps invocation of iptables utility with functions to
append and delete rules; create, clear and delete chains.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
