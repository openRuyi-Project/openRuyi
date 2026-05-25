# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-flowrate
%define go_import_path  github.com/mxk/go-flowrate
%define commit_id       cca7078d478f8520f85629ad7c68962d31ed7682

Name:           go-github-mxk-go-flowrate
Version:        0+git20260607.cca7078
Release:        %autorelease
Summary:        Reader and writer wrappers with flow rate control
License:        BSD-2-Clause
URL:            https://github.com/mxk/go-flowrate
#!RemoteAsset:  sha256:04d0e2ebb1b66b203697ec4161d66fa9cb833071b3393d655aee0c3ab9e7298e
Source0:        https://github.com/mxk/go-flowrate/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Upstreamable test fix: exact timing/rate assertions are sensitive to CI
# scheduler jitter even when flow control works correctly. - HNO3Miracle
Patch0:         0001-make-status-tests-tolerate-scheduler-jitter.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/mxk/go-flowrate) = %{version}

%description
This package provides Go reader and writer wrappers with flow rate
control.

%files
%doc README
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
