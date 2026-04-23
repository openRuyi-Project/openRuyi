# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname urlgrabber

Name:           python-%{srcname}
Version:        4.1.0
Release:        %autorelease
Summary:        A high-level cross-protocol url-grabber
License:        LGPL-2.0-or-later
URL:            https://github.com/rpm-software-management/urlgrabber
#!RemoteAsset:  sha256:075af8afabae6362482d254e5ac3ffa595d1766117b684e53d9c25c2e937e139
Source0:        https://files.pythonhosted.org/packages/source/u/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
A high-level cross-protocol url-grabber for python supporting HTTP, FTP
and file locations.  Features include keepalive, byte ranges, throttling,
authentication, proxies and more.

%generate_buildrequires
%pyproject_buildrequires

%install -a
rm -rf %{buildroot}%{_docdir}/urlgrabber-%{version}

%files -f %{pyproject_files}
%doc ChangeLog README TODO
%license LICENSE
# Extra stuff
%{_bindir}/urlgrabber
%{_libexecdir}/urlgrabber-ext-down

%changelog
%autochangelog
