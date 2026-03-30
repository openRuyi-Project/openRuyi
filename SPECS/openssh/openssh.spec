# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# If we want to enable building these, change this to 1
%bcond kerberos5 0
%bcond fido2 0
%bcond selinux 0
%bcond xorg 0

Name:           openssh
Version:        10.2p1
Release:        %autorelease
Summary:        An open source implementation of SSH protocol version 2
License:        BSD-3-Clause AND BSD-2-Clause AND ISC AND SSH-OpenSSH AND ssh-keyscan AND sprintf AND LicenseRef-openRuyi-Public-Domain AND X11-distribute-modifications-variant
URL:            http://www.openssh.com/portable.html
VCS:            git:https://anongit.mindrot.org/openssh.git
#!RemoteAsset
Source0:        https://ftp.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-%{version}.tar.gz
#!RemoteAsset
Source1:        https://ftp.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-%{version}.tar.gz.asc
Source2:        sshd.pam
Source3:        sshd.service
Source4:        sshd@.service
Source5:        sshd.socket
Source6:        ssh-agent.service
Source7:        ssh-agent.socket
Source8:        sshd.sysconfig
Source9:        sshd-keygen
Source10:       sshd-keygen@.service
Source11:       sshd-keygen.target
Source12:       openssh-server-systemd-sysusers.conf
BuildSystem:    autotools

# Fix seccomp failure termination because of zlib-ng calling hwprobe
# See: https://github.com/openssh/openssh-portable/pull/644
Patch0:         0001-seccomp-sandbox-allow-riscv_hwprobe-syscall-if-prese.patch

# Lets us ship distro config in /etc/ssh/{ssh,sshd}_config.d/*.conf
Patch1:         2000-ssh-sshd-_config-Include-_config.d-.conf.patch

BuildOption(conf):  --sysconfdir=%{_sysconfdir}/ssh
BuildOption(conf):  --libexecdir=%{_libexecdir}/openssh
BuildOption(conf):  --datadir=%{_datadir}/openssh
BuildOption(conf):  --with-default-path=/usr/local/bin:/usr/bin
BuildOption(conf):  --with-superuser-path=/usr/local/bin:/usr/bin
BuildOption(conf):  --with-privsep-path=%{_datadir}/empty.sshd
BuildOption(conf):  --disable-strip
BuildOption(conf):  --without-zlib-version-check
BuildOption(conf):  --without-ipaddr-display
BuildOption(conf):  --with-pie=no
BuildOption(conf):  --without-hardening
BuildOption(conf):  --with-systemd
BuildOption(conf):  --with-pam
%if %{with selinux}
BuildOption(conf):  --with-selinux
BuildOption(conf):  --with-audit=linux
BuildOption(conf):  --with-sandbox=seccomp_filter
%endif
%if %{with kerberos5}
BuildOption(conf):  --with-kerberos5${krb5_prefix:+=${krb5_prefix}}
%else
BuildOption(conf):  --without-kerberos5
%endif
BuildOption(conf):  --with-libedit

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(audit)
BuildRequires:  util-linux
BuildRequires:  groff
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  systemd-rpm-macros
BuildRequires:  make
#BuildRequires:  pkgconfig(p11-kit-1)
%if %{with fido2}
BuildRequires:  pkgconfig(libfido2)
%endif
BuildRequires:  pkgconfig(libxcrypt)
%if %{with kerberos}
BuildRequires:  pkgconfig(krb5)
%endif
BuildRequires:  pkgconfig(libedit)
BuildRequires:  pkgconfig(ncurses)
%if %{with selinux}
BuildRequires:  pkgconfig(libselinux)
%endif
%if %{with xorg}
BuildRequires:  xauth
BuildRequires:  pkgconfig(x11)
%endif

Recommends:     p11-kit

Requires:       openssl
%if %{with selinux}
Requires:       libselinux
Requires:       pkgconfig(audit)
%endif

%description
SSH (Secure SHell) is a program for logging into and executing
commands on a remote machine. SSH is intended to replace rlogin and
rsh, and to provide secure encrypted communications between two
untrusted hosts over an insecure network. X11 connections and
arbitrary TCP/IP ports can also be forwarded over the secure channel.

OpenSSH is OpenBSD's version of the last free version of SSH, bringing
it up to date in terms of security and features.

This package includes the core files necessary for both the OpenSSH
client and server. To make this package useful, you should also
install openssh-clients, openssh-server, or both.

%package        clients
Summary:        An open source SSH client applications
Requires:       openssh = %{version}-%{release}
%systemd_requires
#Requires:       crypto-policies

%description    clients
OpenSSH is a free version of SSH (Secure SHell), a program for logging
into and executing commands on a remote machine. This package includes
the clients necessary to make encrypted connections to SSH servers.

%package        keysign
Summary:        A helper program used for host-based authentication
Requires:       openssh = %{version}-%{release}

%description    keysign
OpenSSH is a free version of SSH (Secure SHell), a program for logging
into and executing commands on a remote machine. ssh-keysign is a
helper program used for host-based authentication disabled by default.

%package        server
Summary:        An open source SSH server daemon
Requires:       openssh = %{version}-%{release}
Requires:       pam
#Requires:       crypto-policies
Requires(pre):  systemd-sysusers
%systemd_requires

%description    server
OpenSSH is a free version of SSH (Secure SHell), a program for logging
into and executing commands on a remote machine. This package contains
the secure shell daemon (sshd). The sshd daemon allows SSH clients to
securely connect to your SSH server.

%package        askpass
Summary:        A passphrase dialog for OpenSSH and X
Requires:       openssh = %{version}-%{release}

%description    askpass
OpenSSH is a free version of SSH (Secure SHell), a program for logging
into and executing commands on a remote machine. This package contains
an X11 passphrase dialog for OpenSSH.

%prep
# Our %%prep won't work so this - 251
%setup -q -n %{name}-%{version}
%autopatch -p1 -q

%conf -p
autoreconf -fiv

%build -p
CFLAGS="$CFLAGS -fPIC"
SAVE_LDFLAGS="$LDFLAGS"
LDFLAGS="$LDFLAGS -pie -z relro -z now"
%if %{with kerberos5}
if test -r /etc/profile.d/krb5-devel.sh ; then
        source /etc/profile.d/krb5-devel.sh
fi
krb5_prefix=`krb5-config --prefix`
if test "$krb5_prefix" != "%{_prefix}" ; then
        CPPFLAGS="$CPPFLAGS -I${krb5_prefix}/include -I${krb5_prefix}/include/gssapi"; export CPPFLAGS
        CFLAGS="$CFLAGS -I${krb5_prefix}/include -I${krb5_prefix}/include/gssapi"
        LDFLAGS="$LDFLAGS -L${krb5_prefix}/%{_lib}"; export LDFLAGS
else
        krb5_prefix=
        CPPFLAGS="-I%{_includedir}/gssapi"; export CPPFLAGS
        CFLAGS="$CFLAGS -I%{_includedir}/gssapi"
fi
%endif

%install -p
mkdir -p -m755 %{buildroot}%{_sysconfdir}/ssh
mkdir -p -m755 %{buildroot}%{_sysconfdir}/ssh/ssh_config.d
mkdir -p -m755 %{buildroot}%{_sysconfdir}/ssh/sshd_config.d
mkdir -p -m755 %{buildroot}%{_libexecdir}/openssh

%install -a
install -d %{buildroot}/etc/pam.d/
install -d %{buildroot}/etc/sysconfig/
install -d %{buildroot}%{_libexecdir}/openssh
install -m644 %{SOURCE2} $RPM_BUILD_ROOT/etc/pam.d/sshd
install -m644 %{SOURCE8} $RPM_BUILD_ROOT/etc/sysconfig/sshd

install -d -m755 $RPM_BUILD_ROOT/%{_unitdir}
install -m644 %{SOURCE3} $RPM_BUILD_ROOT/%{_unitdir}/sshd.service
install -m644 %{SOURCE4} $RPM_BUILD_ROOT/%{_unitdir}/sshd@.service
install -m644 %{SOURCE5} $RPM_BUILD_ROOT/%{_unitdir}/sshd.socket
install -m644 %{SOURCE10} $RPM_BUILD_ROOT/%{_unitdir}/sshd-keygen@.service
install -m644 %{SOURCE11} $RPM_BUILD_ROOT/%{_unitdir}/sshd-keygen.target

install -d -m755 $RPM_BUILD_ROOT/%{_userunitdir}
install -m644 %{SOURCE6} $RPM_BUILD_ROOT/%{_userunitdir}/ssh-agent.service
install -m644 %{SOURCE7} $RPM_BUILD_ROOT/%{_userunitdir}/ssh-agent.socket
install -m744 %{SOURCE9} $RPM_BUILD_ROOT/%{_libexecdir}/openssh/sshd-keygen

install -m755 contrib/ssh-copy-id $RPM_BUILD_ROOT%{_bindir}/
install contrib/ssh-copy-id.1 $RPM_BUILD_ROOT%{_mandir}/man1/

install -m755 contrib/ssh-copy-id $RPM_BUILD_ROOT%{_bindir}/
install contrib/ssh-copy-id.1 $RPM_BUILD_ROOT%{_mandir}/man1/
install -d -m711 ${RPM_BUILD_ROOT}/%{_datadir}/empty.sshd
install -p -D -m 0644 %{SOURCE12} %{buildroot}%{_sysusersdir}/openssh-server.conf

# TODO: We don't need these now but maybe in the future
rm -f $RPM_BUILD_ROOT/etc/profile.d/gnome-ssh-askpass.*

%check
make file-tests
make interop-tests
make extra-tests
make unit
pushd openbsd-compat/regress
make
popd

%pre server
%sysusers_create_package %{name} %{SOURCE12}

%post server
%systemd_post sshd.service sshd.socket

%preun server
%systemd_preun sshd.service sshd.socket

%postun server
%systemd_postun_with_restart sshd.service

%post clients
%systemd_user_post ssh-agent.service
%systemd_user_post ssh-agent.socket

%preun clients
%systemd_user_preun ssh-agent.service
%systemd_user_preun ssh-agent.socket

%files
%license LICENCE
%doc CREDITS ChangeLog OVERVIEW PROTOCOL* README README.platform README.privsep README.tun README.dns TODO
%attr(0755,root,root) %dir %{_sysconfdir}/ssh
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/ssh/moduli
%attr(0755,root,root) %{_bindir}/ssh-keygen
%attr(0644,root,root) %{_mandir}/man1/ssh-keygen.1*
%attr(0755,root,root) %dir %{_libexecdir}/openssh

%files clients
%attr(0755,root,root) %{_bindir}/ssh
%attr(0644,root,root) %{_mandir}/man1/ssh.1*
%attr(0755,root,root) %{_bindir}/scp
%attr(0644,root,root) %{_mandir}/man1/scp.1*
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/ssh/ssh_config
%dir %attr(0755,root,root) %{_sysconfdir}/ssh/ssh_config.d/
%attr(0644,root,root) %{_mandir}/man5/ssh_config.5*
%attr(0755,root,root) %{_bindir}/ssh-agent
%attr(0755,root,root) %{_bindir}/ssh-add
%attr(0755,root,root) %{_bindir}/ssh-keyscan
%attr(0755,root,root) %{_bindir}/sftp
%attr(0755,root,root) %{_bindir}/ssh-copy-id
%attr(0755,root,root) %{_libexecdir}/openssh/ssh-pkcs11-helper
%attr(0755,root,root) %{_libexecdir}/openssh/ssh-sk-helper
%attr(0644,root,root) %{_mandir}/man1/ssh-agent.1*
%attr(0644,root,root) %{_mandir}/man1/ssh-add.1*
%attr(0644,root,root) %{_mandir}/man1/ssh-keyscan.1*
%attr(0644,root,root) %{_mandir}/man1/sftp.1*
%attr(0644,root,root) %{_mandir}/man1/ssh-copy-id.1*
%attr(0644,root,root) %{_mandir}/man8/ssh-pkcs11-helper.8*
%attr(0644,root,root) %{_mandir}/man8/ssh-sk-helper.8*
%attr(0644,root,root) %{_userunitdir}/ssh-agent.service
%attr(0644,root,root) %{_userunitdir}/ssh-agent.socket

%files keysign
%attr(4555,root,root) %{_libexecdir}/openssh/ssh-keysign
%attr(0644,root,root) %{_mandir}/man8/ssh-keysign.8*

%files server
%dir %attr(0711,root,root) %{_datadir}/empty.sshd
%attr(0755,root,root) %{_sbindir}/sshd
%attr(0755,root,root) %{_libexecdir}/openssh/sshd-session
%attr(0755,root,root) %{_libexecdir}/openssh/sshd-auth
%attr(0755,root,root) %{_libexecdir}/openssh/sftp-server
%attr(0755,root,root) %{_libexecdir}/openssh/sshd-keygen
%attr(0644,root,root) %{_mandir}/man5/sshd_config.5*
%attr(0644,root,root) %{_mandir}/man5/moduli.5*
%attr(0644,root,root) %{_mandir}/man8/sshd.8*
%attr(0644,root,root) %{_mandir}/man8/sftp-server.8*
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/ssh/sshd_config
%dir %attr(0700,root,root) %{_sysconfdir}/ssh/sshd_config.d/
%attr(0644,root,root) %config(noreplace) /etc/pam.d/sshd
%attr(0640,root,root) %config(noreplace) /etc/sysconfig/sshd
%attr(0644,root,root) %{_unitdir}/sshd.service
%attr(0644,root,root) %{_unitdir}/sshd@.service
%attr(0644,root,root) %{_unitdir}/sshd.socket
%attr(0644,root,root) %{_unitdir}/sshd-keygen@.service
%attr(0644,root,root) %{_unitdir}/sshd-keygen.target
%attr(0644,root,root) %{_sysusersdir}/openssh-server.conf

%changelog
%{?autochangelog}
