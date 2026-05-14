# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Change these to 1 once we have the dependencies
%bcond avahi 0
%bcond dyninst 0

Name:           systemtap
Version:        5.3
Release:        %autorelease
Summary:        Programmable system-wide instrumentation system
License:        GPL-2.0-or-later
URL:            https://sourceware.org/systemtap/
VCS:            git:https://sourceware.org/git/systemtap.git
#!RemoteAsset:  sha256:966a360fb73a4b65a8d0b51b389577b3c4f92a327e84aae58682103e8c65a69a
Source0:        https://sourceware.org/%{name}/ftp/releases/%{name}-%{version}.tar.gz
#!RemoteAsset:  sha256:81bfd0b93d864f973942bab687713d58dd9b117a354ccfaef7747f058ba01983
Source1:        https://sourceware.org/%{name}/ftp/releases/%{name}-%{version}.tar.gz.asc
BuildSystem:    autotools

BuildOption(conf):  --disable-docs
BuildOption(conf):  --with-python3

BuildRequires:  config
BuildRequires:  make
BuildRequires:  boost-devel
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(libdw)
%if %{with avahi}
BuildRequires:  pkgconfig(avahi-client)
%endif
BuildRequires:  pkgconfig(json-c)
%if %{with dyninst}
BuildRequires:  dyninst-devel
BuildRequires:  pkgconfig(libselinux)
%endif
BuildRequires:  sqlite-devel
BuildRequires:  pkgconfig(systemd)
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

Requires:       %{name}-client = %{version}-%{release}
Requires:       %{name}-devel = %{version}-%{release}

%description
SystemTap is an instrumentation system for systems running Linux.
Developers can write instrumentation scripts to collect data on
the operation of the system.  The base systemtap package contains/requires
the components needed to locally develop and execute systemtap scripts

%package        runtime
Summary:        Programmable system-wide instrumentation system - runtime
Requires(pre):  shadow

%description    runtime
SystemTap runtime contains the components needed to execute
a systemtap script that was already compiled into a module
using a local or remote systemtap-devel installation.

%package        client
Summary:        Programmable system-wide instrumentation system - client
License:        GPL-2.0-or-later AND GPL-2.0-only AND BSD-3-Clause AND LGPL-2.1-only AND GFDL-1.2-or-later AND BSD-2-Clause
Requires:       %{name}-runtime = %{version}-%{release}
# What are these??? - 251
Requires:       coreutils
Requires:       grep
Requires:       sed
Requires:       unzip
Requires:       zip
Requires:       openssh-clients
Requires:       mokutil

%description    client
This package contains/requires only the components needed to
use systemtap scripts by compiling them using a local or a remote
systemtap-server service, then run them using a local or
remote systemtap-runtime.  It includes script samples and
documentation, and a copy of the tapset library for reference.
It does NOT include all the components for running a systemtap
script in a self-contained fashion; for that, use the -devel
subpackage instead.

%package        server
Summary:        Instrumentation System Server
BuildRequires:  pkgconfig(nss)
%if %{with avahi}
BuildRequires:  avahi-devel
%endif
Requires:       %{name}-devel = %{version}-%{release}
Requires:       openssl
Requires:       systemd

%description    server
This is the remote script compilation server component of systemtap.
It announces itself to nearby clients with avahi (if available), and
compiles systemtap scripts to kernel objects on their demand.

%package        devel
Summary:        Programmable system-wide instrumentation system - development headers, tools
License:        GPL-2.0-or-later AND GPL-2.0-only AND BSD-3-Clause AND LGPL-2.1-only AND BSD-2-Clause
Requires:       pkgconfig(libdw)
Requires:       make

%description    devel
This package contains the components needed to compile a systemtap
script from source form into executable (.ko) forms.  It may be
installed on a self-contained developer workstation (along with the
systemtap-client and systemtap-runtime packages), or on a dedicated
remote server (alongside the systemtap-server package).  It includes
a copy of the standard tapset library and the runtime library C files.

%package        exporter
Summary:        Systemtap-prometheus interoperation mechanism
License:        GPL-2.0-or-later
Requires:       %{name}-runtime = %{version}-%{release}

%description    exporter
This package includes files for a systemd service that manages
systemtap sessions and relays prometheus metrics from the sessions
to remote requesters on demand.

%package        runtime-python
Summary:        Systemtap Python Runtime Support
License:        GPL-2.0-or-later
Provides:       %{name}-runtime-python3 = %{version}-%{release}
Requires:       systemtap-runtime = %{version}-%{release}

%description    runtime-python
This package includes support files needed to run systemtap scripts
that probe python processes.

%package        sdt-devel
Summary:        Static probe support header files
License:        GPL-2.0-or-later AND CC0-1.0

%description    sdt-devel
This package includes the <sys/sdt.h> header file used for static
instrumentation compiled into userspace programs.

%package        sdt-dtrace
Summary:        Static probe support dtrace tool
License:        GPL-2.0-or-later AND CC0-1.0
Provides:       dtrace = %{version}-%{release}
Requires:       python3dist(pyparsing)

%description    sdt-dtrace
This package includes the dtrace-compatibility preprocessor
to process related .d files into tracing-macro-laden .h headers.

%conf -p
cp -p %{_bindir}/config.guess .
cp -p %{_bindir}/config.sub .

%install -a
%find_lang %{name} --generate-subpackages --with-man --all-name

mkdir -p %{buildroot}%{_sysconfdir}/stap-server
mkdir -p %{buildroot}%{_localstatedir}/lib/stap-server
mkdir -p %{buildroot}%{_localstatedir}/lib/stap-server/.systemtap
mkdir -p %{buildroot}%{_localstatedir}/log/stap-server
touch %{buildroot}%{_localstatedir}/log/stap-server/log
mkdir -p %{buildroot}%{_localstatedir}/cache/systemtap
mkdir -p %{buildroot}%{_localstatedir}/run/systemtap
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
install -m 644 initscript/logrotate.stap-server %{buildroot}%{_sysconfdir}/logrotate.d/stap-server


mkdir -p %{buildroot}%{_initddir}
install -m 755 initscript/systemtap %{buildroot}%{_initddir}
mkdir -p %{buildroot}%{_sbindir}
ln -sf %{_initddir}/systemtap %{buildroot}%{_sbindir}/systemtap-service

mkdir -p %{buildroot}%{_sysconfdir}/systemtap
mkdir -p %{buildroot}%{_sysconfdir}/systemtap/conf.d
mkdir -p %{buildroot}%{_sysconfdir}/systemtap/script.d
install -m 644 initscript/config.systemtap %{buildroot}%{_sysconfdir}/systemtap/config

install -m 755 initscript/stap-server %{buildroot}%{_initddir}
mkdir -p %{buildroot}%{_sysconfdir}/stap-server/conf.d
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
install -m 644 initscript/config.stap-server %{buildroot}%{_sysconfdir}/sysconfig/stap-server

install -D -m 644 macros.systemtap %{buildroot}%{_rpmmacrodir}/macros.systemtap

%preun exporter
%systemd_preun %{name}-exporter.service

%postun exporter
%systemd_postun_with_restart %{name}-exporter.service

%files
%{_bindir}/stap-jupyter-container
%{_bindir}/stap-jupyter-install
%{_mandir}/man1/stap-jupyter.1*
%dir %{_datadir}/systemtap
%{_datadir}/systemtap/interactive-notebook
# packaged by systemtap-initscript in upstream
%dir %{_localstatedir}/cache/systemtap
%{_initddir}/systemtap
%{_sbindir}/systemtap-service
%config(noreplace) %{_sysconfdir}/systemtap/config

%files runtime -f %{name}.lang
%license COPYING
%doc README README.security AUTHORS NEWS
%{_bindir}/staprun
%{_bindir}/stapsh
%{_bindir}/stap-merge
%{_bindir}/stap-report
%if %{with dyninst}
%{_bindir}/stapdyn
%endif
%{_bindir}/stapbpf
%dir %{_libexecdir}/systemtap
%{_libexecdir}/systemtap/stapio
%{_libexecdir}/systemtap/stap-authorize-cert
%{_mandir}/man1/stap-report.1*
%{_mandir}/man7/error*
%{_mandir}/man7/stappaths.7*
%{_mandir}/man7/warning*
%{_mandir}/man8/stapsh.8*
%{_mandir}/man8/staprun.8*
%if %{with dyninst}
%{_mandir}/man8/stapdyn.8*
%endif
%{_mandir}/man8/stapbpf.8*
%{_mandir}/man8/systemtap-service.8*

%files client
%doc README README.unprivileged AUTHORS NEWS
%license COPYING
%{_datadir}/systemtap/examples
%{_bindir}/stap
%{_bindir}/stap-prep
%{_bindir}/stap-report
%{_mandir}/man1/stap.1*
%{_mandir}/man1/stap-prep.1*
%{_mandir}/man1/stap-merge.1*
%{_mandir}/man1/stap-report.1*
%{_mandir}/man1/stapref.1*
%{_mandir}/man3/*
%{_mandir}/man7/error*
%{_mandir}/man7/stappaths.7*
%{_mandir}/man7/warning*
%dir %{_datadir}/systemtap
%{_datadir}/systemtap/tapset

%files server
%doc README README.unprivileged AUTHORS NEWS
%license COPYING
%{_bindir}/stap-server
%dir %{_libexecdir}/systemtap
%{_libexecdir}/systemtap/stap-serverd
%{_libexecdir}/systemtap/stap-start-server
%{_libexecdir}/systemtap/stap-stop-server
%{_libexecdir}/systemtap/stap-gen-cert
%{_libexecdir}/systemtap/stap-sign-module
%{_libexecdir}/systemtap/stap-env
%{_mandir}/man8/stap-server.8*
%ghost %config(noreplace) %attr(0644,root,root) %{_localstatedir}/log/stap-server/log
%{_initddir}/stap-server
%dir %{_sysconfdir}/stap-server/conf.d
%config(noreplace) %{_sysconfdir}/sysconfig/stap-server
%config(noreplace) %{_sysconfdir}/logrotate.d/stap-server
%dir %{_sysconfdir}/stap-server
%dir %attr(0750,root,root) %{_localstatedir}/lib/stap-server
%dir %attr(0700,root,root) %{_localstatedir}/lib/stap-server/.systemtap
%dir %attr(0755,root,root) %{_localstatedir}/log/stap-server
%ghost %attr(0755,root,root) %{_localstatedir}/run/stap-server
# TODO: Why these are here? I don't think they are provided by avahi - 251
%if %{with avahi}
%{_libexecdir}/systemtap/stap-authorize-cert
%{_mandir}/man7/error*
%{_mandir}/man7/stappaths.7*
%{_mandir}/man7/warning*
%endif

%files devel
%doc README README.unprivileged AUTHORS NEWS
%license COPYING
%{_bindir}/stap
%{_bindir}/stap-prep
%{_bindir}/stap-profile-annotate
%{_bindir}/stap-report
%dir %{_datadir}/systemtap
%{_datadir}/systemtap/runtime
%{_datadir}/systemtap/tapset
%{_mandir}/man1/stap.1*
%{_mandir}/man1/stap-prep.1*
%{_mandir}/man1/stap-report.1*
%{_mandir}/man7/error*
%{_mandir}/man7/stappaths.7*
%{_mandir}/man7/warning*
%{_libexecdir}/systemtap/python/stap-resolve-module-function.py

%files exporter
%{_sysconfdir}/stap-exporter
%{_sysconfdir}/sysconfig/stap-exporter
%{_unitdir}/stap-exporter.service
%{_mandir}/man8/stap-exporter.8*
%{_sbindir}/stap-exporter

%files runtime-python
%{python3_sitearch}/HelperSDT
%{python3_sitearch}/HelperSDT-*.egg-info

%files sdt-devel
%doc README AUTHORS NEWS
%license COPYING
%{_includedir}/sys/sdt.h
%{_includedir}/sys/sdt-config.h
%{_rpmmacrodir}/macros.systemtap

%files sdt-dtrace
%doc README AUTHORS NEWS
%license COPYING
%{_bindir}/dtrace
%{_mandir}/man1/dtrace.1*

%changelog
%autochangelog
