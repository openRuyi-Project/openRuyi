# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           json
%define go_import_path  sigs.k8s.io/json
%define commit_id 2d320260d730f3842fef7b08d9a807bdbc617824

Name:           go-k8s-sigs-json
Version:        0+git20250730.2d32026
Release:        %autorelease
Summary:        Golang JSON decoder supporting case-sensitive, number-preserving, and strict decoding use cases
License:        Apache-2.0
URL:            https://github.com/kubernetes-sigs/json
#!RemoteAsset
Source0:        https://github.com/kubernetes-sigs/json/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(sigs.k8s.io/json) = %{version}

%description
This library is a subproject of sig-api-machinery
(https://github.com/kubernetes/community/tree/master/sig-api-
machinery#json). It provides case-sensitive, integer-preserving JSON
unmarshaling functions based on encoding/json Unmarshal().

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
