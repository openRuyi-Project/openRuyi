# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           pv
Version:        1.10.3
Release:        %autorelease
Summary:        Flexible operating system image builder
License:        GPL-3.0-or-later
URL:            https://www.ivarch.com/programs/pv.shtml
VCS:            git:https://codeberg.org/ivarch/pv.git
#!RemoteAsset
Source0:        https://www.ivarch.com/programs/sources/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gettext

%description
PV ("Pipe Viewer") is a tool for monitoring the progress of data through a
pipeline.

It can be inserted into any normal pipeline between two processes to give a
visual indication of how quickly data is passing through, how long it has
taken, how near to completion it is, and an estimate of how long it will be
until completion.

%install -a
rm %{buildroot}/%{_docdir}/%{name}/INSTALL
%find_lang %{name} --generate-subpackages

%files
%license docs/COPYING
%{_bindir}/%{name}
%{_docdir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%changelog
%autochangelog
