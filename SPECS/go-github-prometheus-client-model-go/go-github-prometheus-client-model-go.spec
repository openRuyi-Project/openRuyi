# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go
%define go_import_path  github.com/prometheus/client_model/go
%define go_source_subdir go
%define commit_id 2d24e7e91dcab27ace797932a2a21081cb959502

Name:           go-github-prometheus-client-model-go
Version:        0+git20260512.2d24e7e
Release:        %autorelease
Summary:        Data model artifacts for Prometheus.
License:        Apache-2.0
URL:            https://github.com/prometheus/client_model
#!RemoteAsset:  sha256:188e242c1b49935caf1ea95662c747a0ce403c5087c2ea50edbc4998ea8aa8e8
Source0:        https://github.com/prometheus/client_model/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n client_model-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(google.golang.org/protobuf/reflect/protoreflect)
BuildRequires:  go(google.golang.org/protobuf/runtime/protoimpl)
BuildRequires:  go(google.golang.org/protobuf/types/known/timestamppb)

Provides:       go(github.com/prometheus/client_model/go) = %{version}

Requires:       go(google.golang.org/protobuf)
Requires:       go(google.golang.org/protobuf/reflect/protoreflect)
Requires:       go(google.golang.org/protobuf/runtime/protoimpl)
Requires:       go(google.golang.org/protobuf/types/known/timestamppb)


%description
*(If you are reading this because you are interested in Prometheus's**
native **histograms, pay special attention to the last paragraph
below.)*

Deprecation note

This repository used to contain the protocol buffer
(https://developers.google.com/protocol-buffers) code that defined both
the data model and the exposition format of Prometheus metrics.

Starting with v2.0.0, the Prometheus server

%install
pushd %{go_source_subdir}
%buildsystem_golangmodules_install
popd

%check
pushd %{go_source_subdir}
%buildsystem_golangmodules_check
popd

%files
%doc README.md
%doc CONTRIBUTING.md
%license LICENSE
%license NOTICE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
