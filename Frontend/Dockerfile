FROM node:18

WORKDIR /app

# Copy package files and install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy the rest of the application
COPY . .

# Expose port
EXPOSE 5173

# Command to start the dev server
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]