# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: ayostl <yao_xp@yeah.net>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           man-pages
Version:        6.15
Release:        %autorelease
Summary:        Linux kernel and user-space C library interfaces documentation
License:        GPL-1.0-or-later AND GPL-2.0-only AND GPL-2.0-or-later AND BSD-2-Clause AND BSD-3-Clause AND BSD-4-Clause-UC AND LGPL-3.0-or-later AND LGPL-3.0-only AND LGPL-3.0-linking-exception AND MIT AND Spencer-94
URL:            https://www.kernel.org/doc/man-pages/
VCS:            git:https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git
#!RemoteAsset
Source0:        https://www.kernel.org/pub/linux/docs/man-pages/%{name}-%{version}.tar.xz
BuildArch:      noarch

BuildRequires:  make

Requires(post): update-alternatives
Requires(postun): update-alternatives
Requires(preun): update-alternatives

%description
The Linux man-pages project documents the Linux kernel and C library interface that
are employed by user-space programs.With respect to the C library, the primary focus is
the GNU C library (glibc), although, where known, documentation of variations on
other C libraries available for Linux is also included.

%prep
%autosetup -p1

%install
%make_install prefix=%{_prefix} -R
rm -f %{buildroot}%{_mandir}/man3/crypt_r.3*
rm -f %{buildroot}%{_mandir}/man3/crypt.3*
rm -f %{buildroot}%{_mandir}/man7/bpf-helpers.7*
rm -f %{buildroot}%{_mandir}/man3/MAX.3*
rm -f %{buildroot}%{_mandir}/man3/MIN.3*

# rename files for alternative usage
mv %{buildroot}%{_mandir}/man7/man.7 %{buildroot}%{_mandir}/man7/man.%{name}.7
touch %{buildroot}%{_mandir}/man7/man.7

%files
%doc README Changes
%{_bindir}/diffman-git
%{_bindir}/mansect
%{_bindir}/pdfman
%{_bindir}/sortman
%ghost %{_mandir}/man7/man.7*
%{_mandir}/man*/*

%pre
# remove alternativized files if they are not symlinks
[ -L %{_mandir}/man7/man.7.gz ] || rm -f %{_mandir}/man7/man.7.gz >/dev/null 2>&1 || :

%post
# set up the alternatives files
%{_sbindir}/update-alternatives --install %{_mandir}/man7/man.7.gz man.7.gz %{_mandir}/man7/man.%{name}.7.gz 300 \
    >/dev/null 2>&1 || :

%preun
if [ $1 -eq 0 ]; then
    %{_sbindir}/update-alternatives --remove man.7.gz %{_mandir}/man7/man.%{name}.7.gz >/dev/null 2>&1 || :
fi

%postun
if [ $1 -ge 1 ]; then
    if [ "$(readlink %{_sysconfdir}/alternatives/man.7.gz)" == "%{_mandir}/man7/man.%{name}.7.gz" ]; then
        %{_sbindir}/update-alternatives --set man.7.gz %{_mandir}/man7/man.%{name}.7.gz >/dev/null 2>&1 || :
    fi
fi

%changelog
%autochangelog
