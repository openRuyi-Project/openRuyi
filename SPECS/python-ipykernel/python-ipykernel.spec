# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname ipykernel

Name:           python-%{srcname}
Version:        6.25.2
Release:        %autorelease
Summary:        IPython kernel for Jupyter
License:        BSD-3-Clause
URL:            https://github.com/ipython/ipykernel
#!RemoteAsset:  sha256:f468ddd1f17acb48c8ce67fcfa49ba6d46d4f9ac0438c1f441be7c3d1372230b
Source0:        https://files.pythonhosted.org/packages/source/i/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l ipykernel ipykernel_launcher

BuildRequires:  gtk3
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(comm)
BuildRequires:  python3dist(debugpy)
BuildRequires:  python3dist(flaky)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(ipyparallel)
BuildRequires:  python3dist(ipython)
BuildRequires:  python3dist(jupyter-client)
BuildRequires:  python3dist(jupyter-core)
BuildRequires:  python3dist(matplotlib)
BuildRequires:  python3dist(matplotlib-inline)
BuildRequires:  python3dist(nest-asyncio)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(psutil)
BuildRequires:  python3dist(pygobject)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pyzmq)
BuildRequires:  python3dist(tornado)
BuildRequires:  python3dist(traitlets)
BuildRequires:  python3dist(trio)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
IPykernel provides the IPython kernel used by Jupyter frontends.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_datadir}/jupyter/kernels/python3/

%changelog
%autochangelog
