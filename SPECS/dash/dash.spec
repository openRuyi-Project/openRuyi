# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           dash
Version:        0.5.13.4
Release:        %autorelease
Summary:        POSIX-compliant implementation of /bin/sh
License:        BSD-3-Clause AND GPL-2.0-or-later
URL:            http://gondor.apana.org.au/~herbert/dash/
VCS:            git:https://git.kernel.org/pub/scm/utils/dash/dash.git
#!RemoteAsset:  sha256:d10dfd41cda59165560db39ca915c2c4a7636fff04281d8d2df77ad92c753e2b
Source0:        http://gondor.apana.org.au/~herbert/dash/files/dash-%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  make

Provides:       /bin/dash

%description
DASH is a POSIX-compliant implementation of /bin/sh that aims to be as small as
possible. It does this without sacrificing speed where possible. In fact, it is
significantly faster than bash (the GNU Bourne-Again SHell) for most tasks.

%post
grep -q '^/bin/dash$' %{_sysconfdir}/shells || \
    echo '/bin/dash' >> %{_sysconfdir}/shells

%postun
if [ $1 -eq 0 ]; then
    sed -i '/^\/bin\/dash$/d' %{_sysconfdir}/shells
fi

%files
%doc ChangeLog
%license COPYING
%{_bindir}/dash
%{_mandir}/man1/dash.1*

%changelog
%autochangelog
