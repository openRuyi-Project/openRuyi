# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: kenlig <qiming.or@isra.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname jupyter_core

Name:           python-jupyter-core
Version:        5.9.1
Release:        %autorelease
Summary:        The base package for Jupyter projects

License:        BSD-3-Clause
URL:            https://github.com/jupyter/jupyter_core
#!RemoteAsset:  sha256:4d09aaff303b9566c3ce657f580bd089ff5c91f5f89cf7d8846c3cdf465b5508
Source:         https://github.com/jupyter/jupyter_core/releases/download/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install): -l jupyter_core jupyter

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(platformdirs)
BuildRequires:  python3dist(traitlets)

%description
Core common functionality of Jupyter projects.
This package contains base application classes and configuration inherited by
other projects.

%package -n python3-jupyter-core
Summary:        The base package for Jupyter projects
Requires:       python3dist(platformdirs)
Requires:       python3dist(traitlets)
Provides:       python3-jupyter-core
%python_provide python3-jupyter-core

%description -n python3-jupyter-core
Core common functionality of Jupyter projects.

This package contains base application classes and configuration inherited by
other projects.

%package -n python-jupyter-filesystem
Summary:        Jupyter filesystem layout

%description -n python-jupyter-filesystem
This package provides directories required by other packages that add
extensions to Jupyter.

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l jupyter_core jupyter

# Create directories for python-jupyter-filesystem package.
install -d %{buildroot}%{_datadir}/jupyter/kernels
install -d %{buildroot}%{_datadir}/jupyter/labextensions/@jupyter
install -d %{buildroot}%{_datadir}/jupyter/nbextensions
install -d %{buildroot}%{_sysconfdir}/jupyter/jupyter_notebook_config.d
install -d %{buildroot}%{_sysconfdir}/jupyter/jupyter_server_config.d
install -d %{buildroot}%{_sysconfdir}/jupyter/nbconfig/common.d
install -d %{buildroot}%{_sysconfdir}/jupyter/nbconfig/edit.d
install -d %{buildroot}%{_sysconfdir}/jupyter/nbconfig/notebook.d
install -d %{buildroot}%{_sysconfdir}/jupyter/nbconfig/terminal.d
install -d %{buildroot}%{_sysconfdir}/jupyter/nbconfig/tree.d

%files -n python3-jupyter-core -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/jupyter
%{_bindir}/jupyter-migrate
%{_bindir}/jupyter-troubleshoot

%files -n python-jupyter-filesystem
%dir %{_datadir}/jupyter
%dir %{_datadir}/jupyter/kernels
%dir %{_datadir}/jupyter/labextensions
%dir %{_datadir}/jupyter/labextensions/@jupyter
%dir %{_datadir}/jupyter/nbextensions
%dir %{_sysconfdir}/jupyter
%dir %{_sysconfdir}/jupyter/jupyter_notebook_config.d
%dir %{_sysconfdir}/jupyter/jupyter_server_config.d
%dir %{_sysconfdir}/jupyter/nbconfig
%dir %{_sysconfdir}/jupyter/nbconfig/common.d
%dir %{_sysconfdir}/jupyter/nbconfig/edit.d
%dir %{_sysconfdir}/jupyter/nbconfig/notebook.d
%dir %{_sysconfdir}/jupyter/nbconfig/terminal.d
%dir %{_sysconfdir}/jupyter/nbconfig/tree.d

%changelog
%autochangelog
