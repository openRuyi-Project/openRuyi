# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: zhangjinqiang <jinqiang.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname distributed

Name:           python-%{srcname}
Version:        2026.3.0
Release:        %autorelease
Summary:        Distributed scheduler for Dask
License:        BSD-3-Clause
URL:            https://distributed.dask.org/
VCS:            git:https://github.com/dask/distributed.git
#!RemoteAsset:  sha256:4a8fc6102fededfbaae45288501276da2297a054d74eb6589f01b087c7f95c26
Source0:        https://files.pythonhosted.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

# No module named 'distributed.bokeh'
BuildOption(check):  -e 'distributed.bokeh'
# No module named 'cupy'
BuildOption(check):  -e 'distributed.protocol.cupy'
# No module named 'keras'
BuildOption(check):  -e 'distributed.protocol.keras'
# No module named 'netCDF4'
BuildOption(check):  -e 'distributed.protocol.netcdf4'
# No module named 'numba.cuda'
BuildOption(check):  -e 'distributed.protocol.numba'
# No module named 'rmm'
BuildOption(check):  -e 'distributed.protocol.rmm'
# No module named 'sparse'
BuildOption(check):  -e 'distributed.protocol.sparse'
# No module named 'distributed.utils_test'
BuildOption(check):  -e 'distributed.utils_test'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(bokeh)
BuildRequires:  python3dist(click)
BuildRequires:  python3dist(cloudpickle)
BuildRequires:  python3dist(dask)
BuildRequires:  python3dist(h5py)
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(locket)
BuildRequires:  python3dist(memray)
BuildRequires:  python3dist(msgpack)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(prometheus-client)
BuildRequires:  python3dist(psutil)
BuildRequires:  python3dist(pyarrow)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(scipy)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(sortedcontainers)
BuildRequires:  python3dist(tblib)
BuildRequires:  python3dist(toolz)
BuildRequires:  python3dist(torch)
BuildRequires:  python3dist(tornado)
BuildRequires:  python3dist(urllib3)
BuildRequires:  python3dist(zict)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Distributed is a lightweight library for distributed computing in Python.
It extends Dask's scheduling capabilities to clusters of machines.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt
%{_bindir}/dask-scheduler
%{_bindir}/dask-ssh
%{_bindir}/dask-worker

%changelog
%autochangelog
