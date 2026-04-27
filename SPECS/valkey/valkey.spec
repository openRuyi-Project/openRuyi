# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# See https://github.com/valkey-io/valkey-doc/tags
%global doc_version 8.1.1

%global make_flags DEBUG="" V="echo" PREFIX=%{buildroot}%{_prefix} BUILD_WITH_SYSTEMD=yes BUILD_TLS=module

%global valkey_modules_abi 1
%global valkey_modules_dir %{_libdir}/%{name}/modules
%global valkey_modules_cfg %{_sysconfdir}/%{name}/modules

# Tests fail in mock, not in local build.
%bcond tests 0
%bcond docs 0
%bcond rdma 0

Name:           valkey
Version:        8.1.4
Release:        %autorelease
Summary:        A persistent key-value database
License:        BSD-3-Clause AND BSD-2-Clause AND MIT AND BSL-1.0
URL:            https://valkey.io
VCS:            git:https://github.com/valkey-io/valkey
#!RemoteAsset:  sha256:32350b017fee5e1a85f7e2d8580d581a0825ceae5cb3395075012c0970694dee
Source0:        https://github.com/valkey-io/valkey/archive/%{version}/valkey-%{version}.tar.gz
Source1:        valkey.logrotate
Source2:        valkey-sentinel.service
Source3:        valkey.service
Source4:        valkey.sysusers
Source5:        valkey.tmpfiles
#!RemoteAsset:  sha256:aa7976a217d399d8079e1c3c9ba3b816ec285e1a197e8a5c378b0d94bd106c7d
Source50:       https://github.com/valkey-io/valkey-doc/archive/%{doc_version}/valkey-doc-%{doc_version}.tar.gz
BuildSystem:    autotools

# Fix default paths in configuration files for RPM layout
Patch0:         valkey-conf.patch
# Workaround to https://github.com/valkey-io/valkey/issues/2678
Patch1:         valkey-loadmod.patch

BuildOption(build):  %{make_flags}
BuildOption(install):  %{make_flags}

BuildRequires:  make
BuildRequires:  gcc
%if %{with tests}
BuildRequires:  procps-ng
BuildRequires:  tcl
%endif
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(openssl)
%if %{with docs}
# for docs/man pages
BuildRequires:  pandoc
BuildRequires:  python3
BuildRequires:  python3dist(pyyaml)
%endif

Provides:       valkey(modules_abi)%{?_isa} = %{valkey_modules_abi}

Requires:       logrotate

%description
Valkey is an advanced key-value store. It is often referred to as a data
structure server since keys can contain strings, hashes, lists, sets and
sorted sets.

You can run atomic operations on these types, like appending to a string;
incrementing the value in a hash; pushing to a list; computing set
intersection, union and difference; or getting the member with highest
ranking in a sorted set.

In order to achieve its outstanding performance, Valkey works with an
in-memory dataset. Depending on your use case, you can persist it either
by dumping the dataset to disk every once in a while, or by appending
each command to a log.

Valkey also supports trivial-to-setup master-slave replication, with very
fast non-blocking first synchronization, auto-reconnection on net split
and so forth.

Other features include Transactions, Pub/Sub, Lua scripting, Keys with a
limited time-to-live, and configuration settings to make Valkey behave like
a cache.

You can use Valkey from most programming languages also.

See https://valkey.io/topics/

%package        devel
Summary:        Development header for Valkey module development
Provides:       %{name}-static = %{version}-%{release}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Header file required for building loadable Valkey modules.

%package        tls
Summary:        TLS module for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Supplements:    %{name}

%description    tls
%summary.

See https://valkey.io/topics/encryption/

%package        compat-redis
Summary:        Conversion script and compatibility symlinks for Redis
Requires:       valkey = %{version}-%{release}
Conflicts:      redis < 7.4
BuildArch:      noarch

%description    compat-redis
%summary

%package        compat-redis-devel
Summary:        Compatibility development header for Redis API Valkey modules
Requires:       valkey-devel = %{version}-%{release}
Conflicts:      redis-devel < 7.4
Conflicts:      redis-static < 7.4
BuildArch:      noarch

%description    compat-redis-devel
Header file required for building loadable Valkey modules with the legacy
Redis API.

%if %{with docs}
%package        doc
Summary:        Documentation and extra man pages for %{name}
BuildArch:      noarch
License:        CC-BY-SA-4.0

%description    doc
%summary
%endif

%prep
# no autosetup due to no support for multiple source extraction
%setup -n %{name}-%{version} -a50
%patch -P0 -p1 -b .rpm
%patch -P1 -p1 -b .loadmod

mv deps/lua/COPYRIGHT             COPYRIGHT-lua
mv deps/jemalloc/COPYING          COPYING-jemalloc
mv deps/hiredis/COPYING COPYING-hiredis-BSD-3-Clause
mv deps/hdr_histogram/LICENSE.txt LICENSE-hdrhistogram
mv deps/hdr_histogram/COPYING.txt COPYING-hdrhistogram
mv deps/fpconv/LICENSE.txt        LICENSE-fpconv

# See https://bugzilla.redhat.com/2240293
# See https://src.fedoraproject.org/rpms/jemalloc/blob/rawhide/f/jemalloc.spec#_34
%ifarch x86_64
sed -e 's/--with-lg-quantum/--with-lg-page=12 --with-lg-quantum/' -i deps/Makefile
%endif

%conf
# Module API version safety check
api=`sed -n -e 's/#define VALKEYMODULE_APIVER_[0-9][0-9]* //p' src/valkeymodule.h`
if test "$api" != "%{valkey_modules_abi}"; then
   : Error: Upstream API version is now ${api}, expecting %%{valkey_modules_abi}.
   : Update the valkey_modules_abi macro, and rebuild.
   exit 1
fi

# Generates macro file
cat << 'EOF' | tee macros.%{name}
%%valkey_version     %version
%%valkey_modules_abi %valkey_modules_abi
%%valkey_modules_dir %valkey_modules_dir
%%valkey_modules_cfg %valkey_modules_cfg
EOF

: TLS configuration file
cat << EOF | tee tls.conf
# TLS module
loadmodule %{valkey_modules_dir}/tls.so
EOF

%build -a

%if %{with docs}
# docs
pushd %{name}-doc-%{doc_version}
# build man pages
%make_build VALKEY_ROOT=../
# build html docs
%make_build html VALKEY_ROOT=../
popd
%endif

%install -a
%if %{with docs}
# install docs
pushd %{name}-doc-%{doc_version}
# man pages
%make_install INSTALL_MAN_DIR=%{buildroot}%{_mandir} VALKEY_ROOT=../
# install html docs
install -d %{buildroot}%{_docdir}/%{name}/
cp -ra _build/html/* %{buildroot}%{_docdir}/%{name}/
# install doc license
install -d %{buildroot}%{_defaultlicensedir}/valkey-doc/
cp -a LICENSE %{buildroot}%{_defaultlicensedir}/valkey-doc/
popd
%endif

# remove sample confs
rm -rf %{buildroot}%{_datadir}/%{name}

# System user
install -p -D -m 0644 %{S:4} %{buildroot}%{_sysusersdir}/%{name}.conf

# Install tmpfiles.d file
install -p -D -m 0644 %{S:5} %{buildroot}%{_tmpfilesdir}/%{name}.conf

# Filesystem.
install -d %{buildroot}%{_sharedstatedir}/%{name}
install -d %{buildroot}%{_localstatedir}/log/%{name}
install -d %{buildroot}%{_localstatedir}/run/%{name}
install -d %{buildroot}%{valkey_modules_dir}

# Install logrotate file.
install -pDm644 %{S:1} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

# Install configuration files.
install -pDm640 %{name}.conf  %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf
install -pDm640 sentinel.conf %{buildroot}%{_sysconfdir}/%{name}/sentinel.conf
install -dm750  %{buildroot}%{valkey_modules_cfg}

# Install systemd unit files.
mkdir -p %{buildroot}%{_unitdir}
install -pm644 %{S:3} %{buildroot}%{_unitdir}
install -pm644 %{S:2} %{buildroot}%{_unitdir}

# Fix non-standard-executable-perm error.
chmod 755 %{buildroot}%{_bindir}/valkey-*

# Install valkey module header
install -pDm644 src/valkeymodule.h %{buildroot}%{_includedir}/valkeymodule.h

# Install rpm macros for valkey modules
#mkdir -p %{buildroot}%{_rpmmacrodir}
install -pDm644 macros.%{name} %{buildroot}%{_rpmmacrodir}/macros.%{name}

# compat header
install -pDm644 src/redismodule.h %{buildroot}%{_includedir}/redismodule.h

# compat systemd symlinks
ln -sr %{buildroot}/usr/lib/systemd/system/valkey.service %{buildroot}/usr/lib/systemd/system/redis.service
ln -sr %{buildroot}/usr/lib/systemd/system/valkey-sentinel.service %{buildroot}/usr/lib/systemd/system/redis-sentinel.service

# TLS module
install -pm755 src/valkey-tls.so %{buildroot}%{valkey_modules_dir}/tls.so
install -pm640 tls.conf          %{buildroot}%{valkey_modules_cfg}/tls.conf

%check
%if %{with tests}
# https://github.com/redis/redis/issues/1417 (for "taskset -c 1")
taskset -c 1 ./runtest --clients 50 --skiptest "Active defrag - AOF loading"
%endif

%pre
%sysusers_create_package %{name} %{SOURCE4}

%post
%systemd_post valkey.service
%systemd_post valkey-sentinel.service

%preun
%systemd_preun valkey.service
%systemd_preun valkey-sentinel.service

%postun
%systemd_postun_with_restart valkey.service
%systemd_postun_with_restart valkey-sentinel.service

%files
%license COPYING
%license COPYRIGHT-lua
%license COPYING-jemalloc
%license LICENSE-hdrhistogram
%license COPYING-hdrhistogram
%license LICENSE-fpconv
%license COPYING-hiredis-BSD-3-Clause
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%attr(0750, valkey, root) %dir %{_sysconfdir}/%{name}
%attr(0750, valkey, root) %dir %{valkey_modules_cfg}
%attr(0640, valkey, root) %config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%attr(0640, valkey, root) %config(noreplace) %{_sysconfdir}/%{name}/sentinel.conf
%dir %{_libdir}/%{name}
%dir %{valkey_modules_dir}
%dir %attr(0750, valkey, valkey) %{_sharedstatedir}/%{name}
%dir %attr(0750, valkey, valkey) %{_localstatedir}/log/%{name}
%{_bindir}/valkey-*
%{_unitdir}/valkey.service
%{_unitdir}/valkey-sentinel.service
%dir %attr(0755, valkey, valkey) %ghost %{_localstatedir}/run/%{name}
%{_sysusersdir}/%{name}.conf
%{_tmpfilesdir}/%{name}.conf
%if %{with docs}
%{_mandir}/man1/valkey*.gz
%{_mandir}/man5/valkey.conf.5.gz
%endif

%if %{with docs}
%files doc
%license LICENSE
%doc %{_docdir}/valkey/
%{_mandir}/man{3,7}/*valkey*.gz
%endif

%files tls
%attr(0640, valkey, root) %config(noreplace) %{valkey_modules_cfg}/tls.conf
%{valkey_modules_dir}/tls.so

%files devel
# main package is not required
%license COPYING
%{_includedir}/valkeymodule.h
%{_rpmmacrodir}/macros.%{name}

%files compat-redis
%{_bindir}/redis-*
%{_unitdir}/redis.service
%{_unitdir}/redis-sentinel.service

%files compat-redis-devel
%{_includedir}/redismodule.h

%changelog
%autochangelog
