# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           whois
Version:        5.6.4
Release:        %autorelease
Summary:        Improved WHOIS client
License:        GPL-2.0-or-later
URL:            https://github.com/rfc1036/whois
#!RemoteAsset
Source0:        https://github.com/rfc1036/whois/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  CONFIG_FILE="%{_sysconfdir}/%{name}.conf"
BuildOption(conf):  HAVE_ICONV=1
BuildOption(conf):  CFLAGS="$RPM_OPT_FLAGS"

BuildRequires:  make
BuildRequires:  coreutils
BuildRequires:  gettext
BuildRequires:  perl-macros
BuildRequires:  perl-devel
BuildRequires:  pkgconfig(libidn2)
BuildRequires:  pkgconfig(libxcrypt)

Requires:       bash-completion
Provides:       mkpasswd = %{version}-%{release}

%description
Searches for an object in a RFC 3912 database.

This version of the WHOIS client tries to guess the right server to ask for
the specified object. If no guess can be made it will connect to
whois.networksolutions.com for NIC handles or whois.arin.net for IPv4
addresses and network names.

%conf
# No conf

%install -a
install -p -m644 -D %{name}.conf %{buildroot}%{_sysconfdir}/%{name}.conf
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
mv %{buildroot}%{_sysconfdir}/bash_completion.d/{mkpasswd,whois} %{buildroot}%{_datadir}/bash-completion/completions

%find_lang %{name} --generate-subpackages

# no tests
%check


%files
%license COPYING debian/copyright
%doc README debian/changelog
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}
%{_bindir}/mkpasswd
%{_mandir}/man1/whois.*
%{_mandir}/man1/mkpasswd.*
%{_mandir}/man5/whois.conf.5.*
%{_datadir}/bash-completion/completions/whois
%{_datadir}/bash-completion/completions/mkpasswd

%changelog
%autochangelog
