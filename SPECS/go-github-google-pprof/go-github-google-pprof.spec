# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global __elf_exclude_path (%{__elf_exclude_path}|^%{go_sys_gopath})
%define _name           pprof
%define go_import_path  github.com/google/pprof
# Upstream does not provide git tags, use commit ID instead - Julian
%define commit_id cb029daf43efe4320650f6b25c6795eddaaf25d7
# TODO: Exclude tests that require additional dependencies - Julian
%define go_test_exclude %{shrink:
    github.com/google/pprof/browsertests
    github.com/google/pprof/internal/binutils
}

Name:           go-github-google-pprof
Version:        0+git20260202.cb029da
Release:        %autorelease
Summary:        pprof is a tool for visualization and analysis of profiling data
License:        Apache-2.0
URL:            https://github.com/google/pprof
#!RemoteAsset
Source0:        https://github.com/google/pprof/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/chzyer/readline)
BuildRequires:  go(github.com/ianlancetaylor/demangle)

Provides:       go(github.com/google/pprof) = %{version}

Requires:       go(github.com/chzyer/readline)
Requires:       go(github.com/ianlancetaylor/demangle)

%description
pprof is a tool for visualization and analysis of profiling data.

pprof reads a collection of profiling samples in profile.proto format
and generates reports to visualize and help analyze the data. It can
generate both text and graphical reports (through the use of the dot
visualization package).

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
