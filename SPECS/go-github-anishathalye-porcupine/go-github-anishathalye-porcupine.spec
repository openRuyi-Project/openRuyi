# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           porcupine
%define go_import_path  github.com/anishathalye/porcupine

Name:           go-github-anishathalye-porcupine
Version:        1.1.0
Release:        %autorelease
Summary:        A fast linearizability checker written in Go
License:        MIT
URL:            https://github.com/anishathalye/porcupine
#!RemoteAsset
Source0:        https://github.com/anishathalye/porcupine/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/anishathalye/porcupine) = %{version}

%description
Porcupine is a fast linearizability checker used in both academia and
industry for testing the correctness of distributed systems. It takes a
sequential specification as executable Go code, along with a concurrent
history, and it determines whether the history is linearizable with
respect to the sequential specification. Porcupine also implements a
visualizer for histories and linearization points.
(click for interactive version)
Porcupine implements the algorithm described in Faster linearizability
checking via P-compositionality (https://arxiv.org/pdf/1504.00204.pdf),
an optimization of the algorithm described in Testing for
Linearizability
(http://www.cs.ox.ac.uk/people/gavin.lowe/LinearizabiltyTesting/paper.
pdf).

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
