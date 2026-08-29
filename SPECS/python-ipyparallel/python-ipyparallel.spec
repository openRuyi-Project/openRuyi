# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname ipyparallel

Name:           python-%{srcname}
Version:        9.2.0
Release:        %autorelease
Summary:        Interactive parallel computing with IPython
License:        BSD-3-Clause
URL:            https://github.com/ipython/ipyparallel
#!RemoteAsset:  sha256:2b31bb4e94708e7ffb4ee6501d7f5f664df7e1c4c572e91e9e0d12484c6a6910
Source0:        https://files.pythonhosted.org/packages/source/i/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# Use the prebuilt labextension from the sdist to break the JupyterLab cycle.
Patch2000:      2000-drop-jupyterlab-build-requirement.patch
# https://github.com/ipython/ipyparallel/pull/1035
Patch2001:      2001-fix-shellcmd-import.patch

BuildOption(install):  -l ipyparallel

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(decorator)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(ipython)
BuildRequires:  python3dist(joblib)
BuildRequires:  python3dist(jupyter-client)
BuildRequires:  python3dist(jupyter-server)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(psutil)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(python-dateutil)
BuildRequires:  python3dist(pyzmq)
BuildRequires:  python3dist(tornado)
BuildRequires:  python3dist(tqdm)
BuildRequires:  python3dist(traitlets)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
IPyParallel provides tools for using IPython to run parallel and distributed
computations interactively.

%prep -a
# Remove ipykernel from build requirements to break the circular dependency.
sed -i '/"ipykernel>=6.9.1",/d' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%install -a
mv %{buildroot}%{_prefix}%{_sysconfdir} %{buildroot}%{_sysconfdir}

# skip tests: No module named 'ipykernel' (circular dependency)
%check

%files -f %{pyproject_files}
%doc README.md
%license COPYING.md
%{_bindir}/ipcluster
%{_bindir}/ipcontroller
%{_bindir}/ipengine
%{_datadir}/jupyter/labextensions/ipyparallel-labextension/
%{_datadir}/jupyter/nbextensions/ipyparallel/
%{_sysconfdir}/jupyter/jupyter_notebook_config.d/ipyparallel.json
%{_sysconfdir}/jupyter/jupyter_server_config.d/ipyparallel.json
%{_sysconfdir}/jupyter/nbconfig/tree.d/ipyparallel.json

%changelog
%autochangelog
