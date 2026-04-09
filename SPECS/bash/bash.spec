# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define baseversion 5.3
%define patchlevel 3

Name:           bash
Version:        %{baseversion}.%{patchlevel}
Release:        %autorelease
Summary:        The GNU Bourne Again shell
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/bash
VCS:            git:https://git.savannah.gnu.org/git/bash.git
#!RemoteAsset
Source0:        https://ftpmirror.gnu.org/gnu/%{name}/%{name}-%{baseversion}.tar.gz
#!RemoteAsset
Source1:        https://ftpmirror.gnu.org/gnu/%{name}/%{name}-%{baseversion}.tar.gz.sig
Source2:        dot.bashrc
Source3:        dot.bash_profile
Source4:        dot.bash_logout
BuildSystem:    autotools

# Official upstream patches
# Patches are converted to apply with '-p1'
Patch1:         0001-bash-5.3-patch-1.patch
Patch2:         0002-bash-5.3-patch-2.patch
Patch3:         0003-bash-5.3-patch-3.patch

# Other patches started from 1000

BuildOption(conf):  --without-bash-malloc

BuildRequires:  autoconf
BuildRequires:  texinfo
BuildRequires:  ncurses-devel
BuildRequires:  glibc-locale
BuildRequires:  make

Requires:       filesystem

Provides:       /bin/sh
Provides:       /bin/bash

%description
The GNU Bourne Again shell (Bash) is a shell or command language
interpreter that is compatible with the Bourne shell (sh). Bash
incorporates useful features from the Korn shell (ksh) and the C shell
(csh). Most sh scripts can be run by bash without modification.

%package        devel
Summary:        Development headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development headers for %{name}.

%prep
%autosetup -n %{name}-%{baseversion} -p1

%conf -p
autoconf

%build -p
bashconfig=(-DDEFAULT_PATH_VALUE=\'\"/usr/local/sbin:/usr/local/bin:/usr/bin\"\'
            -DSTANDARD_UTILS_PATH=\'\"/usr/bin\"\'
            -DSYS_BASHRC=\'\"/etc/bash.bashrc\"\'
            -DSYS_BASH_LOGOUT=\'\"/etc/bash.bash_logout\"\'
            -DNON_INTERACTIVE_LOGIN_SHELLS
            -std=gnu17)

%install -a
ln -sf bash %{buildroot}%{_bindir}/sh
# user configuration file skeletons
mkdir -p %{buildroot}%{_sysconfdir}/skel
install -m 640 %{SOURCE2} %{buildroot}%{_sysconfdir}/skel/.bashrc
install -m 640 %{SOURCE3} %{buildroot}%{_sysconfdir}/skel/.bash_profile
install -m 640 %{SOURCE4} %{buildroot}%{_sysconfdir}/skel/.bash_logout
sed -ri '1{ s@/bin/sh@/bin/bash@ }' %{buildroot}%{_bindir}/bashbug
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
%find_lang %{name} --generate-subpackages

%files
%config(noreplace) /etc/skel/.b*
%license COPYING
%{_bindir}/bash
%{_bindir}/sh
%{_bindir}/bashbug
%{_infodir}/bash.info*
%{_mandir}/*/*
%dir %{_datadir}/doc/*
%{_datadir}/doc/*
%{_datadir}/info/*
%doc RBASH README
%doc doc/{FAQ,INTRO,README,bash{,ref}.html}
%{_libdir}/bash/*

%files devel
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
