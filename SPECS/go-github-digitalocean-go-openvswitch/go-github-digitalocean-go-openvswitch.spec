# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-openvswitch
%define go_import_path  github.com/digitalocean/go-openvswitch
%define go_test_include  %{go_import_path}/ovsdb/...

Name:           go-github-digitalocean-go-openvswitch
Version:        0+git20200422.6b2d502
Release:        %autorelease
Summary:        Go client for Open vSwitch
License:        Apache-2.0
URL:            https://github.com/yousong/go-openvswitch
VCS:            git:https://github.com/yousong/go-openvswitch.git
# Kubecomps replaces the original module with this API-compatible fork.
#!RemoteAsset:  sha256:c14b2845a9c179459d4f927d2c30ec48e8390ea69b1772801d7d093bc143dddf
Source0:        https://github.com/yousong/go-openvswitch/archive/6b2d502be872.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n go-openvswitch-6b2d502be872efc533841c22be6f92da9ecd49b5

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/digitalocean/go-openvswitch) = %{version}

%description
This package provides the github.com/digitalocean/go-openvswitch Go module source.

%files
%doc README.md
%license LICENSE.md
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
