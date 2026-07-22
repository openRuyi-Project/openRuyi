# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname jupyter-client
%global pypi_name jupyter_client

Name:           python-%{srcname}
Version:        8.9.1
Release:        %autorelease
Summary:        Jupyter protocol implementation and client libraries
License:        BSD-3-Clause
URL:            https://github.com/jupyter/jupyter_client
#!RemoteAsset:  sha256:a58f730dd9e728ba16ba1d62ebccf7ffe1ebbdbce4e95cfae941b7321ae1f4fa
Source0:        https://files.pythonhosted.org/packages/source/j/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l jupyter_client

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(jupyter-core)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(python-dateutil)
BuildRequires:  python3dist(pyzmq)
BuildRequires:  python3dist(tornado)
BuildRequires:  python3dist(traitlets)
BuildRequires:  python3dist(typing-extensions)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Jupyter Client implements the Jupyter messaging protocol and client libraries
for communicating with kernels.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/jupyter-kernel
%{_bindir}/jupyter-kernelspec
%{_bindir}/jupyter-run

%changelog
%autochangelog
