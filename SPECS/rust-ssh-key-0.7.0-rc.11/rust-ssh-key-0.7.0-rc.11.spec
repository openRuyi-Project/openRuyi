# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ssh-key
%global full_version 0.7.0-rc.11
%global pkgname ssh-key-0.7.0-rc.11

Name:           rust-ssh-key-0.7.0-rc.11
Version:        0.7.0
Release:        %autorelease
Summary:        Rust crate "ssh-key"
License:        Apache-2.0 OR MIT
URL:            https://github.com/RustCrypto/SSH/tree/master/ssh-key
#!RemoteAsset:  sha256:f9a32fae177b74a22aa9c5b01bf7e68b33545be32d9e381e248058d2adc15ce3
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
Patch2000:      2000-select-released-argon2.patch
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ctutils-0.4) >= 0.4.0
Requires:       crate(sha2-0.11) >= 0.11.0
Requires:       crate(signature-3) >= 3.0.0
Requires:       crate(ssh-cipher-0.3/default) >= 0.3.0
Requires:       crate(ssh-cipher-0.3/encoding) >= 0.3.0
Requires:       crate(ssh-cipher-0.3/zeroize) >= 0.3.0
Requires:       crate(ssh-encoding-0.3/base64) >= 0.3.0
Requires:       crate(ssh-encoding-0.3/ctutils) >= 0.3.0
Requires:       crate(ssh-encoding-0.3/default) >= 0.3.0
Requires:       crate(ssh-encoding-0.3/digest) >= 0.3.0
Requires:       crate(ssh-encoding-0.3/pem) >= 0.3.0
Requires:       crate(ssh-encoding-0.3/zeroize) >= 0.3.0
Requires:       crate(zeroize-1) >= 1.9.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "ssh-key"

%package     -n %{name}+alloc
Summary:        Pure Rust implementation of SSH key file format decoders/encoders as described in RFC4251/RFC4253 and OpenSSH key formats, as well as "sshsig" signatures and certificates (including certificate validation and certificate authority support), with further support for the `authorized_keys` and `known_hosts` file formats - feature "alloc" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(signature-3/alloc) >= 3.0.0
Requires:       crate(ssh-encoding-0.3/alloc) >= 0.3.0
Requires:       crate(ssh-encoding-0.3/base64) >= 0.3.0
Requires:       crate(ssh-encoding-0.3/ctutils) >= 0.3.0
Requires:       crate(ssh-encoding-0.3/digest) >= 0.3.0
Requires:       crate(ssh-encoding-0.3/pem) >= 0.3.0
Requires:       crate(ssh-encoding-0.3/zeroize) >= 0.3.0
Requires:       crate(zeroize-1/alloc) >= 1.9.0
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust ssh-key crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "std" feature.

%package     -n %{name}+crypto
Summary:        Pure Rust implementation of SSH key file format decoders/encoders as described in RFC4251/RFC4253 and OpenSSH key formats, as well as "sshsig" signatures and certificates (including certificate validation and certificate authority support), with further support for the `authorized_keys` and `known_hosts` file formats - feature "crypto"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/ed25519) = %{version}
Requires:       crate(%{pkgname}/p256) = %{version}
Requires:       crate(%{pkgname}/p384) = %{version}
Requires:       crate(%{pkgname}/p521) = %{version}
Requires:       crate(%{pkgname}/rsa) = %{version}
Provides:       crate(%{pkgname}/crypto) = %{version}

%description -n %{name}+crypto
This metapackage enables feature "crypto" for the Rust ssh-key crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Pure Rust implementation of SSH key file format decoders/encoders as described in RFC4251/RFC4253 and OpenSSH key formats, as well as "sshsig" signatures and certificates (including certificate validation and certificate authority support), with further support for the `authorized_keys` and `known_hosts` file formats - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/ecdsa) = %{version}
Requires:       crate(%{pkgname}/rand-core) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust ssh-key crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dsa
Summary:        Pure Rust implementation of SSH key file format decoders/encoders as described in RFC4251/RFC4253 and OpenSSH key formats, as well as "sshsig" signatures and certificates (including certificate validation and certificate authority support), with further support for the `authorized_keys` and `known_hosts` file formats - feature "dsa"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(dsa-0.7.0-rc.16/hazmat) >= 0.7.0-rc.16
Requires:       crate(sha1-0.11/oid) >= 0.11.0
Requires:       crate(signature-3/rand-core) >= 3.0.0
Requires:       crate(ssh-encoding-0.3/base64) >= 0.3.0
Requires:       crate(ssh-encoding-0.3/bigint) >= 0.3.0
Requires:       crate(ssh-encoding-0.3/ctutils) >= 0.3.0
Requires:       crate(ssh-encoding-0.3/digest) >= 0.3.0
Requires:       crate(ssh-encoding-0.3/pem) >= 0.3.0
Requires:       crate(ssh-encoding-0.3/zeroize) >= 0.3.0
Provides:       crate(%{pkgname}/dsa) = %{version}

%description -n %{name}+dsa
This metapackage enables feature "dsa" for the Rust ssh-key crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ecdsa
Summary:        Pure Rust implementation of SSH key file format decoders/encoders as described in RFC4251/RFC4253 and OpenSSH key formats, as well as "sshsig" signatures and certificates (including certificate validation and certificate authority support), with further support for the `authorized_keys` and `known_hosts` file formats - feature "ecdsa"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sec1-0.8/point) >= 0.8.0
Provides:       crate(%{pkgname}/ecdsa) = %{version}

%description -n %{name}+ecdsa
This metapackage enables feature "ecdsa" for the Rust ssh-key crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ed25519
Summary:        Pure Rust implementation of SSH key file format decoders/encoders as described in RFC4251/RFC4253 and OpenSSH key formats, as well as "sshsig" signatures and certificates (including certificate validation and certificate authority support), with further support for the `authorized_keys` and `known_hosts` file formats - feature "ed25519"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rand-core) = %{version}
Requires:       crate(ed25519-dalek-3.0.0-rc.1) >= 3.0.0-rc.1
Provides:       crate(%{pkgname}/ed25519) = %{version}

%description -n %{name}+ed25519
This metapackage enables feature "ed25519" for the Rust ssh-key crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+encryption
Summary:        Pure Rust implementation of SSH key file format decoders/encoders as described in RFC4251/RFC4253 and OpenSSH key formats, as well as "sshsig" signatures and certificates (including certificate validation and certificate authority support), with further support for the `authorized_keys` and `known_hosts` file formats - feature "encryption"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/rand-core) = %{version}
Requires:       crate(bcrypt-pbkdf-0.11/alloc) >= 0.11.0
Requires:       crate(ssh-cipher-0.3/aes) >= 0.3.0
Requires:       crate(ssh-cipher-0.3/chacha20poly1305) >= 0.3.0
Requires:       crate(ssh-cipher-0.3/encoding) >= 0.3.0
Requires:       crate(ssh-cipher-0.3/zeroize) >= 0.3.0
Provides:       crate(%{pkgname}/encryption) = %{version}

%description -n %{name}+encryption
This metapackage enables feature "encryption" for the Rust ssh-key crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+getrandom
Summary:        Pure Rust implementation of SSH key file format decoders/encoders as described in RFC4251/RFC4253 and OpenSSH key formats, as well as "sshsig" signatures and certificates (including certificate validation and certificate authority support), with further support for the `authorized_keys` and `known_hosts` file formats - feature "getrandom"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rand-core) = %{version}
Requires:       crate(ssh-cipher-0.3/encoding) >= 0.3.0
Requires:       crate(ssh-cipher-0.3/getrandom) >= 0.3.0
Requires:       crate(ssh-cipher-0.3/zeroize) >= 0.3.0
Provides:       crate(%{pkgname}/getrandom) = %{version}

%description -n %{name}+getrandom
This metapackage enables feature "getrandom" for the Rust ssh-key crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+p256
Summary:        Pure Rust implementation of SSH key file format decoders/encoders as described in RFC4251/RFC4253 and OpenSSH key formats, as well as "sshsig" signatures and certificates (including certificate validation and certificate authority support), with further support for the `authorized_keys` and `known_hosts` file formats - feature "p256"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/ecdsa) = %{version}
Requires:       crate(p256-0.14.0-rc.15/ecdsa) >= 0.14.0-rc.15
Provides:       crate(%{pkgname}/p256) = %{version}

%description -n %{name}+p256
This metapackage enables feature "p256" for the Rust ssh-key crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+p384
Summary:        Pure Rust implementation of SSH key file format decoders/encoders as described in RFC4251/RFC4253 and OpenSSH key formats, as well as "sshsig" signatures and certificates (including certificate validation and certificate authority support), with further support for the `authorized_keys` and `known_hosts` file formats - feature "p384"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/ecdsa) = %{version}
Requires:       crate(p384-0.14.0-rc.15/ecdsa) >= 0.14.0-rc.15
Provides:       crate(%{pkgname}/p384) = %{version}

%description -n %{name}+p384
This metapackage enables feature "p384" for the Rust ssh-key crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+p521
Summary:        Pure Rust implementation of SSH key file format decoders/encoders as described in RFC4251/RFC4253 and OpenSSH key formats, as well as "sshsig" signatures and certificates (including certificate validation and certificate authority support), with further support for the `authorized_keys` and `known_hosts` file formats - feature "p521"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/ecdsa) = %{version}
Requires:       crate(p521-0.14.0-rc.15/ecdsa) >= 0.14.0-rc.15
Provides:       crate(%{pkgname}/p521) = %{version}

%description -n %{name}+p521
This metapackage enables feature "p521" for the Rust ssh-key crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ppk
Summary:        Pure Rust implementation of SSH key file format decoders/encoders as described in RFC4251/RFC4253 and OpenSSH key formats, as well as "sshsig" signatures and certificates (including certificate validation and certificate authority support), with further support for the `authorized_keys` and `known_hosts` file formats - feature "ppk"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(argon2-0.6/alloc) >= 0.6.0
Requires:       crate(hex-0.4/alloc) >= 0.4.0
Requires:       crate(hmac-0.13/default) >= 0.13.0
Requires:       crate(sha1-0.11/oid) >= 0.11.0
Requires:       crate(ssh-cipher-0.3/aes) >= 0.3.0
Requires:       crate(ssh-cipher-0.3/encoding) >= 0.3.0
Requires:       crate(ssh-cipher-0.3/zeroize) >= 0.3.0
Provides:       crate(%{pkgname}/ppk) = %{version}

%description -n %{name}+ppk
This metapackage enables feature "ppk" for the Rust ssh-key crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-core
Summary:        Pure Rust implementation of SSH key file format decoders/encoders as described in RFC4251/RFC4253 and OpenSSH key formats, as well as "sshsig" signatures and certificates (including certificate validation and certificate authority support), with further support for the `authorized_keys` and `known_hosts` file formats - feature "rand_core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-core-0.10) >= 0.10.0
Requires:       crate(ssh-cipher-0.3/encoding) >= 0.3.0
Requires:       crate(ssh-cipher-0.3/rand-core) >= 0.3.0
Requires:       crate(ssh-cipher-0.3/zeroize) >= 0.3.0
Provides:       crate(%{pkgname}/rand-core) = %{version}

%description -n %{name}+rand-core
This metapackage enables feature "rand_core" for the Rust ssh-key crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rsa
Summary:        Pure Rust implementation of SSH key file format decoders/encoders as described in RFC4251/RFC4253 and OpenSSH key formats, as well as "sshsig" signatures and certificates (including certificate validation and certificate authority support), with further support for the `authorized_keys` and `known_hosts` file formats - feature "rsa"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/rand-core) = %{version}
Requires:       crate(rsa-0.10.0-rc.18/sha2) >= 0.10.0-rc.18
Requires:       crate(ssh-encoding-0.3/base64) >= 0.3.0
Requires:       crate(ssh-encoding-0.3/bigint) >= 0.3.0
Requires:       crate(ssh-encoding-0.3/ctutils) >= 0.3.0
Requires:       crate(ssh-encoding-0.3/digest) >= 0.3.0
Requires:       crate(ssh-encoding-0.3/pem) >= 0.3.0
Requires:       crate(ssh-encoding-0.3/zeroize) >= 0.3.0
Provides:       crate(%{pkgname}/rsa) = %{version}

%description -n %{name}+rsa
This metapackage enables feature "rsa" for the Rust ssh-key crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Pure Rust implementation of SSH key file format decoders/encoders as described in RFC4251/RFC4253 and OpenSSH key formats, as well as "sshsig" signatures and certificates (including certificate validation and certificate authority support), with further support for the `authorized_keys` and `known_hosts` file formats - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.16
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust ssh-key crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha1
Summary:        Pure Rust implementation of SSH key file format decoders/encoders as described in RFC4251/RFC4253 and OpenSSH key formats, as well as "sshsig" signatures and certificates (including certificate validation and certificate authority support), with further support for the `authorized_keys` and `known_hosts` file formats - feature "sha1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sha1-0.11/oid) >= 0.11.0
Provides:       crate(%{pkgname}/sha1) = %{version}

%description -n %{name}+sha1
This metapackage enables feature "sha1" for the Rust ssh-key crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tdes
Summary:        Pure Rust implementation of SSH key file format decoders/encoders as described in RFC4251/RFC4253 and OpenSSH key formats, as well as "sshsig" signatures and certificates (including certificate validation and certificate authority support), with further support for the `authorized_keys` and `known_hosts` file formats - feature "tdes"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/encryption) = %{version}
Requires:       crate(ssh-cipher-0.3/encoding) >= 0.3.0
Requires:       crate(ssh-cipher-0.3/tdes) >= 0.3.0
Requires:       crate(ssh-cipher-0.3/zeroize) >= 0.3.0
Provides:       crate(%{pkgname}/tdes) = %{version}

%description -n %{name}+tdes
This metapackage enables feature "tdes" for the Rust ssh-key crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
