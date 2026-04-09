# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           fgprof
%define go_import_path  github.com/felixge/fgprof

Name:           go-github-felixge-fgprof
Version:        0.9.5
Release:        %autorelease
Summary:        🚀 fgprof is a sampling Go profiler that allows you to analyze On-CPU as well as Off-CPU (e.g. I/O) time together.
License:        MIT
URL:            https://github.com/felixge/fgprof
#!RemoteAsset
Source0:        https://github.com/felixge/fgprof/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/pprof)
BuildRequires:  go(github.com/stretchr/testify)

Provides:       go(github.com/felixge/fgprof) = %{version}

Requires:       go(github.com/google/pprof)

%description
fgprof is a sampling Go profiler that allows you to analyze On-CPU as well as Off-CPU (e.g. I/O) time together.

Go's builtin sampling CPU profiler can only show On-CPU time, but it's better than fgprof at that. Go also includes tracing profilers that can analyze I/O, but they can't be combined with the CPU profiler.

fgprof is designed for analyzing applications with mixed I/O and CPU workloads. This kind of profiling is also known as wall-clock profiling.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
