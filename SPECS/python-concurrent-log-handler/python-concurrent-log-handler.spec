# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname concurrent-log-handler
%global pypi_name concurrent_log_handler

Name:           python-%{srcname}
Version:        0.9.29
Release:        %autorelease
Summary:        Concurrent log handler with file rotation support
License:        Apache-2.0
URL:            https://github.com/Preston-Landers/concurrent-log-handler
#!RemoteAsset:  sha256:bc37a76d3f384cbf4a98f693ebd770543edc0f4cd5c6ab6bc70e9e1d7d582265
Source0:        https://files.pythonhosted.org/packages/source/c/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(hatchling)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Concurrent Log Handler provides logging handlers for Python's standard
logging module that safely write to a shared log file from multiple
processes and threads, with size-based and time-based rotation support.

%generate_buildrequires
%pyproject_buildrequires -r

%files -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
