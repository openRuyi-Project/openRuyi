# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit        a2287c3041a3f2a204eb942e09c015eab00dc7dd
%global shortcommit   %(c=%{commit}; echo ${c:0:7})

Name:           config
Version:        20250710+git%{shortcommit}
Release:        %autorelease
Summary:        Ubiquitous config.guess and config.sub scripts
License:        GPL-2.0-or-later
URL:            https://savannah.gnu.org/projects/config
#!RemoteAsset:  git+https://git.savannah.gnu.org/git/config.git#%{commit}
#!CreateArchive
Source0:        config-%{commit}.tar.gz

BuildRequires:  make
BuildRequires:  help2man

%description
The `config.guess` script tries to guess a canonical system triple, and
`config.sub` validates and canonicalizes it. These are used as part of
configuration in nearly all GNU packages (and many others).

%prep
%setup -q -n config-%{commit}
# Fix the shebang to use /usr/bin/env
sed -i '1s|^#!/bin/sh$|#!/usr/bin/env sh|' testsuite/config-guess.sh || true

%build
make manpages

%install
mkdir -p %{buildroot}%{_bindir}
install -m755 config.guess %{buildroot}%{_bindir}/config.guess
install -m755 config.sub   %{buildroot}%{_bindir}/config.sub

mkdir -p %{buildroot}%{_mandir}/man1
install -m644 doc/config.guess.1 %{buildroot}%{_mandir}/man1/config.guess.1
install -m644 doc/config.sub.1   %{buildroot}%{_mandir}/man1/config.sub.1

%files
%{_bindir}/config.guess
%{_bindir}/config.sub
%{_mandir}/man1/config.guess.1*
%{_mandir}/man1/config.sub.1*

%changelog
%autochangelog
