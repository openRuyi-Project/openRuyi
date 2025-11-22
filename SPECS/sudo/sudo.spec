# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           sudo
Version:        1.9.17p2
Release:        %autorelease
Summary:        Allows restricted root access for specified users
License:        ISC
URL:            https://www.sudo.ws
#!RemoteAsset
Source0:        https://www.sudo.ws/dist/%{name}-%{version}.tar.gz
Source1:        sudoers.conf
Source2:        sudo.pam
Source3:        sudo-i.pam

# NOTE: Temporarily disable applying CVE patches below.
# These patches (CVE-2025-32462 / CVE-2025-32463) have not yet been checked
# against the latest upstream version.
# Until verification is done, do not apply them to avoid conflicts.
# TODO: Re-enable if upstream has not fixed the issues.
# Patch0:         0001-CVE-2025-32462.patch
# Patch1:         0002-CVE-2025-32463.patch

BuildSystem:    autotools
BuildRequires:  pam-devel groff flex bison automake autoconf libtool
BuildRequires:  libcap-devel libselinux-devel gettext zlib-devel
Requires:       pam
Recommends:     vim-minimal
Requires(post): coreutils

BuildOption(conf): --disable-root-mailer
BuildOption(conf): --disable-intercept
BuildOption(conf): --disable-log-server
BuildOption(conf): --disable-log-client
BuildOption(conf): --with-logging=syslog
BuildOption(conf): --with-logfac=authpriv
BuildOption(conf): --with-pam
BuildOption(conf): --with-pam-login
BuildOption(conf): --with-editor=/bin/vi
BuildOption(conf): --with-env-editor
BuildOption(conf): --with-ignore-dot
BuildOption(conf): --with-tty-tickets
BuildOption(conf): --without-ldap
BuildOption(conf): --with-selinux
BuildOption(conf): --with-passprompt="[sudo] password for %p: "
BuildOption(conf): --without-linux-audit
BuildOption(conf): --with-sssd

BuildOption(install): install_uid=`id -u` install_gid=`id -g` sudoers_uid=`id -u` sudoers_gid=`id -g`

%description
Sudo is a program designed to allow a sysadmin to give limited root privileges
to users and log root activity. The basic philosophy is to give as few
privileges as possible but still allow people to get their work done.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains header files for developing sudo plugins.

%conf -p
autoreconf -I m4 -fv --install
export CFLAGS="%{build_cflags} -fpie" LDFLAGS="%{build_ldflags} -pie"

%install -a
# Set correct permissions
chmod 755 %{buildroot}%{_bindir}/* %{buildroot}%{_sbindir}/*
# Create required directories
install -p -d -m 700 %{buildroot}/var/db/sudo/lectured
install -p -d -m 750 %{buildroot}%{_sysconfdir}/sudoers.d
install -p -d -m 755 %{buildroot}%{_sysconfdir}/dnf/protected.d/
# Install sudoers config
install -p -c -m 0440 %{S:1} %{buildroot}/etc/sudoers
# Install dnf protection config
echo sudo > sudo.conf
install -p -c -m 0644 sudo.conf %{buildroot}/etc/dnf/protected.d/
rm -f sudo.conf
# Fix permissions on plugins
chmod +x %{buildroot}%{_libexecdir}/sudo/*.so
# Clean up unwanted files
rm -f %{buildroot}%{_datadir}/examples/sudo
# Replace the broken %delete_la macro with its correct implementation
find %{buildroot} -type f -name "*.la" -delete -print
rm -f %{buildroot}%{_sysconfdir}/sudoers.dist
# Add ld.so.conf.d entry for plugins
mkdir -p %{buildroot}/etc/ld.so.conf.d
echo "/usr/libexec/sudo" > %{buildroot}/etc/ld.so.conf.d/%{name}-%{_arch}.conf
# Install PAM files
mkdir -p %{buildroot}/etc/pam.d
install -p -c -m 0644 %{S:2} %{buildroot}/etc/pam.d/sudo
install -p -c -m 0644 %{S:3} %{buildroot}/etc/pam.d/sudo-i

%find_lang sudo --all-name --generate-subpackages
# Remove rpath
# chrpath --delete %{buildroot}%{_bindir}/* %{buildroot}%{_sbindir}/* %{buildroot}%{_libexecdir}/sudo/*

%post
/bin/chmod 0440 /etc/sudoers || :
/sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license LICENSE.md
%doc README.md ChangeLog NEWS
%doc plugins/sample/sample_plugin.c
/usr/share/doc/sudo/
%attr(0440,root,root) %config(noreplace) /etc/sudoers
%attr(0750,root,root) %dir /etc/sudoers.d/
%config(noreplace) /etc/dnf/protected.d/sudo.conf
%config(noreplace) /etc/sudo.conf
%attr(4111,root,root) %{_bindir}/sudo
%attr(0111,root,root) %{_bindir}/sudoreplay
%{_bindir}/sudoedit
%{_bindir}/cvtsudoers
%{_sbindir}/visudo
%{_libexecdir}/sudo/sesh
%{_libexecdir}/sudo/sudo_noexec.so
%{_libexecdir}/sudo/sudoers.so
%{_libexecdir}/sudo/group_file.so
%{_libexecdir}/sudo/system_group.so
%{_libexecdir}/sudo/audit_json.so
%{_libexecdir}/sudo/libsudo_util.so*
%dir /var/db/sudo
%dir /var/db/sudo/lectured
%dir %{_libexecdir}/sudo
%config(noreplace) /etc/pam.d/sudo
%config(noreplace) /etc/pam.d/sudo-i
%config(noreplace) /etc/ld.so.conf.d/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man8/*

%files devel
%{_includedir}/sudo_plugin.h

%changelog
%{?autochangelog}
