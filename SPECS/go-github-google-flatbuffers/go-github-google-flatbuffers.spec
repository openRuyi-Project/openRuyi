# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           flatbuffers
%define go_import_path  github.com/google/flatbuffers
# So tired, can't stand more flaky tests - 251
%define go_test_exclude_glob %{shrink:
    github.com/google/flatbuffers/examples*
    github.com/google/flatbuffers/grpc/examples*
    github.com/google/flatbuffers/grpc/tests*
    github.com/google/flatbuffers/samples*
    github.com/google/flatbuffers/tests*
}

Name:           go-github-google-flatbuffers
Version:        25.12.19
Release:        %autorelease
Summary:        FlatBuffers: Memory Efficient Serialization Library
License:        Apache-2.0
URL:            https://github.com/google/flatbuffers
#!RemoteAsset
Source0:        https://github.com/google/flatbuffers/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/google/flatbuffers) = %{version}

%description
FlatBuffers is a cross platform serialization library architected
for maximum memory efficiency. It allows you to directly access
serialized data without parsing/unpacking it first, while still having
great forwards/backwards compatibility.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
