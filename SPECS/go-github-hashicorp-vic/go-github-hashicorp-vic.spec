# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           vic
%define go_import_path  github.com/hashicorp/vic
# It's a fork, and the test have not compitable with upstream - Julian
%define go_test_ignore_failure 1

Name:           go-github-hashicorp-vic
Version:        1.5.0
Release:        %autorelease
Summary:        vSphere Integrated Containers Engine is a container runtime for vSphere.
License:        Apache-2.0
URL:            https://github.com/hashicorp/vic
#!RemoteAsset
Source0:        https://github.com/hashicorp/vic/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/hashicorp/vic) = %{version}

%description
HashiCorp Fork Changes

This fork exists only to solve hashicorp/go-discover#94. vmware/vic
imports logrus with upper case Sirupsen which conflicts with almost all
other libraries at this point and goes against the general
recommendation for interop (https://github.com/sirupsen/logrus#case-
sensitivity). The issues is tracked in vmware/vic#8263 once the upstream
has found a solution to that, this fork will be removed. Given the
ugliness of upstrea having to update (maybe even raise issues and PR
against) lots of deps or modify their imports in the vendor dir we are
forking for now to solve our immediate problem.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
