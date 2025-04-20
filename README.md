# HWSSO (Hardware Single Sign-On)

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Build Status](https://travis-ci.org/Lions2025/hwsso.svg?branch=master)](https://travis-ci.org/Lions2025/hwsso)
[![Release Version](https://img.shields.io/github/release/Lions2025/hwsso.svg)](https://github.com/Lions2025/hwsso/releases)

**HWSSO** 是一个基于硬件的安全单点登录解决方案，支持跨平台身份认证与授权管理。通过整合硬件安全模块（HSM）和标准协议，为企业级应用提供高安全性的身份验证服务。

## 🚀 主要特性

- ✅ **硬件级安全**：支持 YubiKey、TPM 2.0 等硬件设备
- ✅ **多协议兼容**：OAuth 2.0、OpenID Connect、SAML 2.0
- ✅ **多因素认证**：生物识别/U2F/OTP 组合验证
- ✅ **跨平台支持**：Windows/Linux/macOS 原生集成
- ✅ **审计日志**：完整记录所有认证事件
- ✅ **高可用架构**：支持集群部署和负载均衡

## 📦 快速安装

### 系统要求
- Java 11+ 或 Go 1.18+
- PostgreSQL 12+
- Redis 6+
- Docker 20.10+

### 通过 Docker 部署
```bash
# 拉取最新镜像
docker pull yuanjs2025/hwsso:latest

# 启动服务（配置环境变量）
docker run -d -p 8080:8080 \
  -e DB_URL=jdbc:postgresql://db-host:5432/hwsso \
  -e REDIS_HOST=redis-host \
  yuanjs2025/hwsso
