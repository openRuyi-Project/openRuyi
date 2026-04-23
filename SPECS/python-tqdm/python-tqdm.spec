# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname tqdm

Name:           python-%{srcname}
Version:        4.67.1
Release:        %autorelease
Summary:        Fast, Extensible Progress Meter
License:        MPL-2.0 AND MIT
URL:            https://github.com/tqdm/tqdm
#!RemoteAsset:  sha256:f8aef9c52c08c13a65f30ea34f4e5aac3fd1a34959879d7e59e63027286627f2
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
# Needs additional dependencies
BuildOption(check):  -e "tqdm.contrib.*" -e "tqdm.dask" -e "tqdm.keras" -e "tqdm.tk"

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools-scm[toml])
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(colorama)
BuildRequires:  python3dist(rich)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
tqdm derives from the Arabic word taqaddum which can
mean “progress,” and is an abbreviation for “I love you so much”
in Spanish (te quiero demasiado). Instantly make your loops show
a smart progress meter - just wrap any iterable with
tqdm(iterable), and you’re done!

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENCE
%{_bindir}/tqdm

%changelog
%autochangelog
