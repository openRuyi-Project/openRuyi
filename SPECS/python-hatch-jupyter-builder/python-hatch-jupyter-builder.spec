# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname hatch-jupyter-builder
%global pypi_name hatch_jupyter_builder

Name:           python-%{srcname}
Version:        0.9.1
Release:        %autorelease
Summary:        Hatch plugin for building Jupyter packages
License:        BSD-3-Clause
URL:            https://github.com/jupyterlab/hatch-jupyter-builder
#!RemoteAsset:  sha256:79278198d124c646b799c5e8dca8504aed9dcaaa88d071a09eb0b5c2009a58ad
Source0:        https://files.pythonhosted.org/packages/source/h/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l hatch_jupyter_builder
# This test case only works during migration
BuildOption(check):  -e 'hatch_jupyter_builder.migrate.jupyter_packaging'

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(tomli-w)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
hatch-jupyter-builder is a Hatch plugin for building Jupyter packages and
prebuilt extensions.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE.txt
%{_bindir}/hatch-jupyter-builder

%changelog
%autochangelog
