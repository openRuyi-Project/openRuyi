# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname threadpoolctl

Name:           python-%{srcname}
Version:        3.5.0
Release:        %autorelease
Summary:        Thread-pool Controls
License:        BSD-3-Clause
URL:            https://github.com/joblib/threadpoolctl
#!RemoteAsset:  sha256:082433502dd922bf738de0d8bcc4fdcbf0979ff44c42bd40f5af8a282f6fa107
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Python helpers to limit the number of threads used in the
threadpool-backed of common native libraries used for scientific computing
and data science (e.g. BLAS and OpenMP).
Fine control of the underlying thread-pool size can be useful in
workloads that involve nested parallelism so as to mitigate
oversubscription issues.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md multiple_openmp.md

%changelog
%autochangelog
