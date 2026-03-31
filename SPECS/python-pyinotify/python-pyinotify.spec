# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pyinotify

Name:           python-%{srcname}
Version:        0.9.6
Release:        %autorelease
Summary:        Monitor filesystem events with Python under Linux
License:        MIT
URL:            https://github.com/seb-m/pyinotify
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
This is a Python module for watching filesystems changes. By its design
pyinotify can be used for any kind of fs monitoring.

%prep -a
sed -i '1c#! %{__python3}' python3/pyinotify.py
sed -i "s|#!%{_bindir}/env python|#!%__python2|" python2/examples/*py
sed -i "s|#!%{_bindir}/env python|#!%__python3|" python3/examples/*py

%generate_buildrequires
%pyproject_buildrequires

# TODO: Add python-asyncore
%check

%files -f %{pyproject_files}
%doc ACKS README.md

%changelog
%{?autochangelog}
